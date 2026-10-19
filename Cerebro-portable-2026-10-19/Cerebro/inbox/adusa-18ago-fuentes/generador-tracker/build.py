# -*- coding: utf-8 -*-
import zipfile, shutil, re, math, os
import xml.etree.ElementTree as ET
from content import HEADER, SUMMARY, CELLS

SRC="/Users/MancoMenStudio/Downloads/Appriss ADUSA-Support-Tracker - 08182026.xlsx"
OUT="/Users/MancoMenStudio/Downloads/Appriss ADUSA-Support-Tracker - 08182026 PM.xlsx"

NS="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
ET.register_namespace('', NS)
def q(t): return f"{{{NS}}}{t}"

z=zipfile.ZipFile(SRC)
shared=[]
ss=ET.fromstring(z.read('xl/sharedStrings.xml'))
for si in ss.findall(q('si')):
    shared.append(''.join(t.text or '' for t in si.iter(q('t'))))

root=ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
sheetData=root.find(q('sheetData'))

# column widths for wrap estimation
WID={'A':11,'B':28,'C':19,'D':18,'E':14,'F':10,'G':10,'H':45,'I':47,'J':29}

def cellref(row,col): return f"{col}{row}"

def get_cell(rowel,col):
    for c in rowel.findall(q('c')):
        if re.match(r'^([A-Z]+)',c.get('r')).group(1)==col: return c
    return None

def set_inline(c,text):
    for ch in list(c): c.remove(ch)
    c.set('t','inlineStr')
    is_=ET.SubElement(c,q('is')); t=ET.SubElement(is_,q('t'))
    t.set('{http://www.w3.org/XML/1998/namespace}space','preserve')
    t.text=text

def set_num(c,val):
    for ch in list(c): c.remove(ch)
    if 't' in c.attrib: del c.attrib['t']
    v=ET.SubElement(c,q('v')); v.text=str(val)

def cur_text(c):
    if c is None: return ''
    if c.get('t')=='s':
        v=c.find(q('v'))
        return shared[int(v.text)] if v is not None else ''
    if c.get('t')=='inlineStr':
        t=c.find(q('is'))
        return ''.join(x.text or '' for x in t.iter(q('t'))) if t is not None else ''
    v=c.find(q('v'))
    return v.text if v is not None else ''

# ---- convert every existing shared-string cell to inline so we can edit freely
for rowel in sheetData.findall(q('row')):
    for c in rowel.findall(q('c')):
        if c.get('t')=='s':
            set_inline(c,cur_text(c))

rows={int(r.get('r')):r for r in sheetData.findall(q('row'))}

# ---- header lines
for (r,col),txt in HEADER.items():
    set_inline(get_cell(rows[r],col),txt)

# ---- summary table
for r,(theme,tk,res,pen,awa,act) in SUMMARY.items():
    set_inline(get_cell(rows[r],'A'),theme)
    for col,val in zip(['C','D','E','F','G'],[tk,res,pen,awa,act]):
        set_num(get_cell(rows[r],col),val)

# ---- detail cells
for r,cols in CELLS.items():
    rowel=rows[r]
    for col,val in cols.items():
        c=get_cell(rowel,col)
        if c is None:
            # create it, borrowing style from the J column of same row band
            ref=cellref(r,col)
            c=ET.SubElement(rowel,q('c')); c.set('r',ref)
            sib=get_cell(rowel,'I')
            base={'H':'I','I':'H','J':'I','C':'B','D':'D','G':'F','E':'E'}.get(col,'I')
            b=get_cell(rowel,base)
            if b is not None and b.get('s'): c.set('s',b.get('s'))
            # keep cells ordered
            rowel[:] = sorted(rowel, key=lambda e: (
                sum((ord(ch)-64)*26**i for i,ch in enumerate(reversed(re.match(r'^([A-Z]+)',e.get('r')).group(1))))
            ))
        if isinstance(val,int): set_num(c,val)
        else: set_inline(c,val)

# ---- D column colour must follow the value
DSTYLE={'Resolved':'19','Pending Ahold verification':'28','Active with Appriss':'29','Awaiting Ahold input':'30'}
for r,rowel in rows.items():
    if r<23: continue
    d=get_cell(rowel,'D')
    if d is None: continue
    txt=cur_text(d)
    if txt in DSTYLE: d.set('s',DSTYLE[txt])

# ---- recompute row heights from content
LADDER=[58.5,72,84.75,97.5,110.25,123,135.75,148.5,161.25,174,186.75,199.5,212.25,225]
for r,rowel in rows.items():
    if r<23: continue
    if get_cell(rowel,'B') is None: continue   # section header row
    mx=1
    for col in ['B','H','I','J']:
        c=get_cell(rowel,col)
        if c is None: continue
        txt=cur_text(c)
        cpl=max(8,int(WID[col]*1.02))
        n=0
        for part in txt.split('\n'):
            n+=max(1,math.ceil(len(part)/cpl))
        mx=max(mx,n)
    idx=min(len(LADDER)-1,max(0,mx-4))
    rowel.set('ht',str(LADDER[idx])); rowel.set('customHeight','1')

# ---- write package
if os.path.exists(OUT): os.remove(OUT)
zin=zipfile.ZipFile(SRC)
zout=zipfile.ZipFile(OUT,'w',zipfile.ZIP_DEFLATED)
new_sheet=ET.tostring(root,encoding='UTF-8',xml_declaration=True)
for item in zin.infolist():
    data=zin.read(item.filename)
    if item.filename=='xl/worksheets/sheet1.xml':
        data=new_sheet
    zout.writestr(item,data)
zout.close()
print("written:",OUT, os.path.getsize(OUT),"bytes")
