"""
Post-process brand-test.pptx to inject 11 named slide layouts.
Each layout gets the correct background image, so PowerPoint shows
branded thumbnails when the user clicks "Add New Slide".
"""

import os, sys, shutil, zipfile, re
from lxml import etree

# Accept CLI args: inject-layouts.py <source.pptx> <dest.pptx>
# Falls back to defaults relative to the skill root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.dirname(SCRIPT_DIR)

SRC        = sys.argv[1] if len(sys.argv) > 1 else os.path.join(SKILL_ROOT, "output", "brand-test.pptx")
DEST       = sys.argv[2] if len(sys.argv) > 2 else os.path.join(SKILL_ROOT, "output", "brand-test-layouts.pptx")
WORK       = os.path.join(SKILL_ROOT, "output", "layout-work")
ASSETS     = os.path.join(SKILL_ROOT, "assets", "backgrounds")
THEME_XML  = os.path.join(SKILL_ROOT, "assets", "appriss-theme1.xml")

# ── Layout definitions ────────────────────────────────────────────────────────
# (name, background_file, slide_number_that_uses_it)
LAYOUTS = [
    ("Cover Dark",       "cover-dark1.png",       1),
    ("Light Content",    "primary-light-01.png",  2),
    ("Dark Content",     "primary-dark-02.png",   3),
    ("Stats Light",      "primary-light-02.png",  4),
    ("Closing Dark",     "cover-dark3.png",       5),
    ("Co-branded Cover", "cover-dark2.png",       6),
    ("Section Divider",  "cover-dark4.png",       7),
    ("Two Column",       "primary-light-01.png",  8),
    ("Quote Callout",    "primary-dark-01.png",   9),
    ("Data Table",       "primary-light-02.png",  10),
    ("Speaker",          "primary-light-01.png",  11),
]

# XML namespaces
NSMAP = {
    "a":  "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r":  "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "p":  "http://schemas.openxmlformats.org/presentationml/2006/main",
    "pkg": "http://schemas.openxmlformats.org/package/2006/relationships",
}
REL_NS  = "http://schemas.openxmlformats.org/package/2006/relationships"
TYPE_LAYOUT = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout"
TYPE_IMAGE  = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image"

# ── Step 0: unzip to work dir ────────────────────────────────────────────────
if os.path.exists(WORK):
    shutil.rmtree(WORK)
with zipfile.ZipFile(SRC) as z:
    z.extractall(WORK)

# ── Step 0.5: inject Appriss brand theme XML ─────────────────────────────────
# Overwrites the pptxgenjs-generated theme with the real Appriss color/font scheme
# so PowerPoint shows Appriss colors in the theme color picker.
theme_dir = os.path.join(WORK, "ppt", "theme")
os.makedirs(theme_dir, exist_ok=True)
shutil.copy(THEME_XML, os.path.join(theme_dir, "theme1.xml"))

# ── Step 1: copy background images into ppt/media ───────────────────────────
media_dir = os.path.join(WORK, "ppt", "media")
os.makedirs(media_dir, exist_ok=True)

# Map bg filename → rId image filename inside media
bg_to_media = {}
for i, (name, bg_file, _) in enumerate(LAYOUTS, 1):
    if bg_file not in bg_to_media:
        src_path = os.path.join(ASSETS, bg_file)
        dest_name = f"layoutBg{i}.png"
        shutil.copy(src_path, os.path.join(media_dir, dest_name))
        bg_to_media[bg_file] = dest_name

# Also copy the crown icon if not there
crown_src  = os.path.join(SKILL_ROOT, "assets", "appriss-crown-gray.png")
crown_dest = os.path.join(media_dir, "crownGray.png")
if not os.path.exists(crown_dest):
    shutil.copy(crown_src, crown_dest)

# ── Step 2: update [Content_Types].xml to include new layouts ───────────────
ct_path = os.path.join(WORK, "[Content_Types].xml")
ct_tree = etree.parse(ct_path)
ct_root = ct_tree.getroot()
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"

# Ensure PNG override exists
png_ct = "image/png"
existing_types = {el.get("Extension") for el in ct_root.findall(f"{{{CT_NS}}}Default")}
if "png" not in existing_types:
    ct_root.append(etree.SubElement(ct_root, f"{{{CT_NS}}}Default",
                                    Extension="png", ContentType="image/png"))

layout_ct = "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"
for i in range(1, len(LAYOUTS) + 1):
    part_name = f"/ppt/slideLayouts/slideLayout{i}.xml"
    # Check if already exists
    existing = [el for el in ct_root.findall(f"{{{CT_NS}}}Override")
                if el.get("PartName") == part_name]
    if not existing:
        ct_root.append(etree.SubElement(ct_root, f"{{{CT_NS}}}Override",
                                        PartName=part_name, ContentType=layout_ct))

ct_tree.write(ct_path, xml_declaration=True, encoding="UTF-8", standalone=True)

# ── Step 3: create slideLayout XML files ────────────────────────────────────
layouts_dir = os.path.join(WORK, "ppt", "slideLayouts")
layouts_rels_dir = os.path.join(layouts_dir, "_rels")
os.makedirs(layouts_dir, exist_ok=True)
os.makedirs(layouts_rels_dir, exist_ok=True)

def make_layout_xml(name):
    """Minimal slideLayout XML. Background image uses rId2; rId1 is reserved for slideMaster ref."""
    xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
             xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
             xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
             preserve="1">
  <p:cSld name="{name}">
    <p:bg>
      <p:bgPr>
        <a:blipFill dpi="0" rotWithShape="1">
          <a:blip r:embed="rId2"><a:lum/></a:blip>
          <a:srcRect/>
          <a:stretch><a:fillRect/></a:stretch>
        </a:blipFill>
        <a:effectLst/>
      </p:bgPr>
    </p:bg>
    <p:spTree>
      <p:nvGrpSpPr>
        <p:cNvPr id="1" name=""/>
        <p:cNvGrpSpPr/>
        <p:nvPr/>
      </p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/>
                <a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm>
      </p:grpSpPr>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sldLayout>'''
    return xml

def make_layout_rels(image_filename):
    """Rels: rId1 = back-reference to slide master (REQUIRED), rId2 = background image."""
    xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1"
    Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster"
    Target="../slideMasters/slideMaster1.xml"/>
  <Relationship Id="rId2"
    Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image"
    Target="../media/{image_filename}"/>
</Relationships>'''
    return xml

# Write all 11 layout files
for i, (name, bg_file, _) in enumerate(LAYOUTS, 1):
    layout_path = os.path.join(layouts_dir, f"slideLayout{i}.xml")
    rels_path   = os.path.join(layouts_rels_dir, f"slideLayout{i}.xml.rels")

    with open(layout_path, "w", encoding="utf-8") as f:
        f.write(make_layout_xml(name))

    media_filename = bg_to_media[bg_file]
    with open(rels_path, "w", encoding="utf-8") as f:
        f.write(make_layout_rels(media_filename))

# ── Step 4: update slideMaster rels to reference all 11 layouts ─────────────
master_rels_path = os.path.join(WORK, "ppt", "slideMasters", "_rels", "slideMaster1.xml.rels")
mr_tree = etree.parse(master_rels_path)
mr_root = mr_tree.getroot()

# Remove existing layout relationships
for rel in mr_root.findall(f"{{{REL_NS}}}Relationship"):
    if rel.get("Type") == TYPE_LAYOUT:
        mr_root.remove(rel)

# Find the max rId currently in use
existing_ids = []
for r in mr_root.findall(f"{{{REL_NS}}}Relationship"):
    rid = r.get("Id", "")
    try:
        existing_ids.append(int(rid.lstrip("rId")))
    except ValueError:
        pass
next_id = max(existing_ids, default=0) + 1

layout_rids = {}
for i in range(1, len(LAYOUTS) + 1):
    rid = f"rId{next_id}"
    layout_rids[i] = rid
    etree.SubElement(mr_root, f"{{{REL_NS}}}Relationship",
                     Id=rid, Type=TYPE_LAYOUT,
                     Target=f"../slideLayouts/slideLayout{i}.xml")
    next_id += 1

mr_tree.write(master_rels_path, xml_declaration=True, encoding="UTF-8", standalone=True)

# ── Step 5: update slideMaster1.xml sldLayoutIdLst ──────────────────────────
master_path = os.path.join(WORK, "ppt", "slideMasters", "slideMaster1.xml")
sm_tree = etree.parse(master_path)
sm_root = sm_tree.getroot()

P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
id_lst = sm_root.find(f"{{{P_NS}}}sldLayoutIdLst")
if id_lst is None:
    id_lst = etree.SubElement(sm_root, f"{{{P_NS}}}sldLayoutIdLst")
else:
    # Clear existing
    for child in list(id_lst):
        id_lst.remove(child)

base_layout_id = 2147483648
for i in range(1, len(LAYOUTS) + 1):
    rid = layout_rids[i]
    etree.SubElement(id_lst, f"{{{P_NS}}}sldLayoutId",
                     id=str(base_layout_id + i),
                     attrib={"{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id": rid})

sm_tree.write(master_path, xml_declaration=True, encoding="UTF-8", standalone=True)

# ── Step 6: point each slide's rels at the correct layout ───────────────────
slides_rels_dir = os.path.join(WORK, "ppt", "slides", "_rels")

for i, (name, bg_file, slide_num) in enumerate(LAYOUTS, 1):
    rels_file = os.path.join(slides_rels_dir, f"slide{slide_num}.xml.rels")
    if not os.path.exists(rels_file):
        print(f"  Warning: {rels_file} not found, skipping")
        continue

    sr_tree = etree.parse(rels_file)
    sr_root = sr_tree.getroot()

    # Find existing layout rel and reuse its rId (preserves numeric format)
    # If none exists, pick the next available numeric rId
    existing_layout_rel = None
    existing_rids = set()
    for rel in sr_root.findall(f"{{{REL_NS}}}Relationship"):
        rid = rel.get("Id", "")
        existing_rids.add(rid)
        if rel.get("Type") == TYPE_LAYOUT:
            existing_layout_rel = rel

    if existing_layout_rel is not None:
        # Reuse the existing rId, just update the target
        existing_layout_rel.set("Target", f"../slideLayouts/slideLayout{i}.xml")
    else:
        # Find next available numeric rId
        used_nums = set()
        for rid in existing_rids:
            try:
                used_nums.add(int(rid.replace("rId", "")))
            except ValueError:
                pass
        next_num = max(used_nums, default=0) + 1
        while f"rId{next_num}" in existing_rids:
            next_num += 1
        etree.SubElement(sr_root, f"{{{REL_NS}}}Relationship",
                         Id=f"rId{next_num}",
                         Type=TYPE_LAYOUT,
                         Target=f"../slideLayouts/slideLayout{i}.xml")

    sr_tree.write(rels_file, xml_declaration=True, encoding="UTF-8", standalone=True)

# ── Step 7: repack ────────────────────────────────────────────────────────────
if os.path.exists(DEST):
    os.remove(DEST)

with zipfile.ZipFile(DEST, "w", zipfile.ZIP_DEFLATED) as zout:
    for root_dir, dirs, files in os.walk(WORK):
        for file in files:
            file_path = os.path.join(root_dir, file)
            arcname  = os.path.relpath(file_path, WORK)
            zout.write(file_path, arcname)

print(f"Done: {DEST}")
print(f"  Layouts injected: {len(LAYOUTS)}")
for i, (name, bg, slide) in enumerate(LAYOUTS, 1):
    print(f"  {i:2}. '{name}' ({bg}) → slide {slide}")
