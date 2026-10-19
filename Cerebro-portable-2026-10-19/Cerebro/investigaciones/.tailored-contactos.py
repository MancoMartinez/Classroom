from PIL import Image, ImageOps, ImageDraw
from pathlib import Path
import json
root=Path('/Users/MancoMenStudio/Cerebro')
out=root/'investigaciones/2026-10-16-tailored-galeria'
out.mkdir(exist_ok=True)
manifest=json.loads((root/'investigaciones/2026-10-16-tailored-adjuntos-manifest.json').read_text())
manifest+=json.loads((root/'investigaciones/2026-10-16-tailored-extra-evidencia.json').read_text())['extra']
for ticket in sorted(set(a['ticket'] for a in manifest)):
    items=[a for a in manifest if a['ticket']==ticket and a['path'].endswith('.png') and (root/a['path']).exists()]
    for start in range(0,len(items),6):
        group=items[start:start+6]
        sheet=Image.new('RGB',(1800,1500),'#dadde2');d=ImageDraw.Draw(sheet)
        for i,a in enumerate(group):
            im=Image.open(root/a['path']).convert('RGB');im.thumbnail((885,450))
            x=(i%2)*900;y=(i//2)*500
            sheet.paste(im,(x+(900-im.width)//2,y+35))
            d.text((x+10,y+8),a['id']+' '+a['filename'],fill='black')
        sheet.save(out/f'{ticket}-{start//6+1}.jpg',quality=90)
missing=[a for a in manifest if not (root/a['path']).exists()]
(out/'cobertura.json').write_text(json.dumps({'inventario':len(manifest),'existentes':len(manifest)-len(missing),'faltantes':missing},indent=2))
print(len(manifest),len(missing))
