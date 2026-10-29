"""Build original, code-drawn profile artwork and a synthetic BIM example.

Python 3 + Pillow. Run from any directory. No model or third-party image inputs.
"""
from pathlib import Path
from html import escape
import csv
import math
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / 'assets'
EXAMPLES = ROOT / 'examples'
ASSETS.mkdir(exist_ok=True)
EXAMPLES.mkdir(exist_ok=True)
NAVY, TEAL, AMBER = '#0b1628', '#5eead4', '#f7bd64'

def text(x, y, value, size=22, color='#e8f0fa', weight=400, extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" {extra}>{escape(value)}</text>'

def svg(body, width=1200, height=340, title='BIM engineering illustration'):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">Original schematic artwork; no project model or application screenshot.</desc>
<defs><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M 32 0 L 0 0 0 32" fill="none" stroke="#24364e" stroke-width="0.6"/></pattern></defs>
<rect width="100%" height="100%" rx="18" fill="{NAVY}"/><rect width="100%" height="100%" rx="18" fill="url(#grid)" opacity="0.45"/>
<g font-family="Segoe UI,Arial,sans-serif">{body}</g></svg>'''

def line(points, color, width=2, opacity=1, dash=''):
    pts = ' '.join(f'{x:.1f},{y:.1f}' for x,y in points)
    return f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" opacity="{opacity}" stroke-dasharray="{dash}"/>'

def building():
    out=''
    def p(x,y,z): return (895 + (x-y)*0.78, 265 + (x+y)*0.31 - z)
    for z in (0,62,124,186):
        out += line([p(0,0,z),p(190,0,z),p(190,150,z),p(0,150,z),p(0,0,z)],'#667c99',1.5,0.8)
    for x,y in ((0,0),(190,0),(190,150),(0,150)):
        out += line([p(x,y,0),p(x,y,186)],'#667c99',1.5,0.8)
    for z in (48,110,172):
        out += line([p(28,100,z),p(150,100,z),p(150,30,z)],TEAL,6)
        out += line([p(85,145,z-17),p(85,15,z-17),p(180,15,z-17)],AMBER,10,0.85)
    out += line([p(28,100,25),p(28,100,193)],TEAL,6)
    out += f'<circle cx="{p(85,100,110)[0]}" cy="{p(85,100,110)[1]}" r="15" fill="none" stroke="{AMBER}" stroke-dasharray="3 5"/>'
    return out

for theme in ('dark','light'):
    body = text(54,54,'AH / BIM DEVELOPMENT',18,TEAL,600, 'letter-spacing="3"')
    body += text(50,132,'Ahmed Hisham',62,weight=650)
    body += text(54,180,'BIM Developer Engineer',29,'#c9d7e9')
    body += text(54,222,'Revit tools. Engineering logic. Coordinated models.',21,'#a4b5cd')
    for x,w,label in ((54,145,'C# / .NET'),(211,125,'Python'),(348,146,'Revit API')):
        body += f'<rect x="{x}" y="256" width="{w}" height="38" rx="8" fill="#14283d" stroke="#2b445f"/>'
        body += text(x+15,282,label,18,TEAL,600)
    body += '<g transform="translate(110 -15) scale(.85)">' + building() + '</g>'
    body += text(830,315,'MODEL → CODE → REVIEW',15,'#a4b5cd',500,'letter-spacing="2"')
    output=svg(body,title='Ahmed Hisham — BIM Developer Engineer')
    if theme=='light':
        output=output.replace(NAVY,'#f1f6fc').replace('#e8f0fa','#12233c').replace('#c9d7e9','#304560').replace('#a4b5cd','#465e7b').replace(TEAL,'#087f75').replace('#14283d','#e0edf7').replace('#24364e','#bbcbdd').replace('#2b445f','#c4d6e7')
    (ASSETS/f'header-{theme}.svg').write_text(output,encoding='utf-8')

cards=[
 ('clashresolveai','01 / REVIT ADD-IN','ClashResolveAI','Detect. Inspect. Track.','C# · .NET 4.8 · Revit API · WPF',TEAL),
 ('bim-engine','02 / PYREVIT EXTENSION','BIM Engine','Geometry meets a review workflow.','Python · C# · Octrees · SQLite',AMBER),
 ('plumbing-engine','03 / ENGINEERING APPLICATION','Plumbing AI Engineer','From calculation to traceable review.','Python · SQLite · Streamlit · BIM mapping','#9fb6ff')
]
for key,kicker,title,sub,stack,color in cards:
    body = text(46,43,kicker,16,color,600,'letter-spacing="2"')
    body += text(43,100,title,46,weight=650)
    body += text(46,144,sub,23,'#c9d7e9')
    body += text(46,193,stack,18,'#a4b5cd')
    if key=='clashresolveai':
        body += line([(850,195),(850,65),(1065,65)],color,18)
        body += line([(800,115),(1100,175)],AMBER,26,0.85)
        body += '<rect x="825" y="98" width="70" height="63" rx="8" fill="#f8717120" stroke="#fb7185" stroke-dasharray="5 5"/>'
        body += text(928,215,'SPATIAL REVIEW',14,'#a4b5cd',500,'letter-spacing="2"')
    elif key=='bim-engine':
        for x,y,w in ((810,50,235),(810,50,117),(927,50,118),(810,167,118)):
            body += f'<rect x="{x}" y="{y}" width="{w}" height="{w/2}" fill="none" stroke="#4c6685"/>'
        body += line([(835,190),(920,190),(920,85),(1080,85)],TEAL,8)
        body += f'<circle cx="920" cy="145" r="24" fill="{NAVY}" stroke="{color}" stroke-width="2"/>'
        body += text(914,153,'+',25,color)
    else:
        body += line([(800,187),(800,55),(1100,55)],'#4c6685',2)
        body += line([(805,174),(850,158),(895,135),(940,105),(985,79),(1040,68),(1090,65)],color,4)
        for x,y in ((850,158),(940,105),(1040,68)):
            body += f'<circle cx="{x}" cy="{y}" r="6" fill="{NAVY}" stroke="{color}" stroke-width="3"/>'
        body += text(935,210,'INPUT → RESULT → REVIEW',13,'#a4b5cd',500,'letter-spacing="1"')
    (ASSETS/f'{key}.svg').write_text(svg(body,height=245,title=title+' — schematic project cover'),encoding='utf-8')

# A small, closed, outward-wound mesh made from separate rectangular solids.
# A duct passes below a structural beam; a service route sits below the duct.
SOLIDS = [
 ('structural_beam',(-110,-14,72),(110,14,100)),
 ('duct',(-32,-100,38),(32,100,62)),
 ('service_main',(-105,-60,12),(105,-50,22)),
 ('service_branch',(-85,-50,12),(-75,85,22)),
]
FACETS=[]
def add_box(lo,hi):
    x,y,z=lo; X,Y,Z=hi
    v=[(x,y,z),(X,y,z),(X,Y,z),(x,Y,z),(x,y,Z),(X,y,Z),(X,Y,Z),(x,Y,Z)]
    for quad in ((0,3,2,1),(4,5,6,7),(0,1,5,4),(3,7,6,2),(0,4,7,3),(1,2,6,5)):
        for ids in ((quad[0],quad[1],quad[2]),(quad[0],quad[2],quad[3])):
            a,b,c=[v[i] for i in ids]
            u=[b[i]-a[i] for i in range(3)]; w=[c[i]-a[i] for i in range(3)]
            n=(u[1]*w[2]-u[2]*w[1],u[2]*w[0]-u[0]*w[2],u[0]*w[1]-u[1]*w[0])
            length=math.sqrt(sum(t*t for t in n)); n=tuple(t/length for t in n)
            FACETS.append((n,(a,b,c)))
for _,lo,hi in SOLIDS: add_box(lo,hi)
stl=['solid synthetic_service_zone']
for n,vs in FACETS:
    stl += ['  facet normal '+' '.join(f'{t:g}' for t in n),'    outer loop']
    stl += ['      vertex '+' '.join(f'{t:g}' for t in v) for v in vs]
    stl += ['    endloop','  endfacet']
stl += ['endsolid synthetic_service_zone']
(EXAMPLES/'service-zone.stl').write_text('\n'.join(stl)+'\n',encoding='utf-8')

rows=[
 ['DEMO-001','L03','Pipe','Duct','Open','Review routing at service crossing'],
 ['DEMO-002','L03','Duct','Beam','Reviewed','Inspect vertical separation'],
 ['DEMO-003','L04','Cable tray','Pipe','Open','Review support and routing'],
 ['DEMO-004','L04','Pipe','Beam','Resolved','Illustrative revised route recorded'],
 ['DEMO-005','L05','Duct','Cable tray','Reviewed','Coordination decision pending'],
 ['DEMO-006','L05','Pipe','Pipe','Open','Review crossing and service intent'],
]
with (EXAMPLES/'coordination-issues.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.writer(f);writer.writerow(['Issue ID','Level','Element A','Element B','Status','Review note']);writer.writerows(rows)

# Animated schematic, deliberately separate from the tools' real UI.
FONT_DIR=Path('C:/Windows/Fonts')
def font(size,bold=False):
    return ImageFont.truetype(str(FONT_DIR/('segoeuib.ttf' if bold else 'segoeui.ttf')),size)
def project(x,y,z): return (670+(x-y)*0.74, 310+(x+y)*0.30-z*1.4)
def draw_box(draw,lo,hi,color):
    x,y,z=lo;X,Y,Z=hi
    verts=[(x,y,z),(X,y,z),(X,Y,z),(x,Y,z),(x,y,Z),(X,y,Z),(X,Y,Z),(x,Y,Z)]
    for idx,factor in (((0,1,5,4),0.65),((1,2,6,5),0.8),((4,5,6,7),1.0)):
        rgb=tuple(int(int(color[i:i+2],16)*factor) for i in (1,3,5))
        draw.polygon([project(*verts[i]) for i in idx],fill=rgb,outline='#b6c7da')
frames=[]
for phase in range(3):
    for step in range(12):
        im=Image.new('RGB',(960,480),NAVY);d=ImageDraw.Draw(im)
        for x in range(0,960,32):d.line((x,0,x,480),fill='#14263b')
        for y in range(0,480,32):d.line((0,y,960,y),fill='#14263b')
        d.text((36,26),'COORDINATION / GEOMETRY STUDY',font=font(17,True),fill=TEAL)
        titles=['01 / Find candidates','02 / Inspect overlap','03 / Review a revision']
        d.text((36,80),titles[phase],font=font(30,True),fill='#e8f0fa')
        descriptions=[['Bounding envelopes narrow','the search to nearby elements.'],['A candidate is not a confirmed','hard clash. Check the solids.'],['This illustration separates','the routes vertically.']]
        for k,t in enumerate(descriptions[phase]):d.text((38,135+k*29),t,font=font(21),fill='#c9d7e9')
        shift=0 if phase<2 else 30*min(1,step/7)
        draw_box(d,(-120,-16,65),(120,16,88),'#657e9e')
        draw_box(d,(-27,-105,52-shift),(27,105,76-shift),TEAL)
        if phase==0:
            a=project(-40,-112,82);b=project(40,112,48)
            d.rectangle((min(a[0],b[0])-30,min(a[1],b[1])-35,max(a[0],b[0])+30,max(a[1],b[1])+20),outline=AMBER,width=2)
        if phase==1:
            p=project(0,0,65);r=25+step%4*2
            d.ellipse((p[0]-r,p[1]-r,p[0]+r,p[1]+r),outline='#fb7185',width=3)
        d.text((38,247),['CANDIDATE PAIR','GEOMETRY REVIEW','ILLUSTRATIVE REVISION'][phase],font=font(16,True),fill=AMBER)
        d.text((38,287),'C# / Python / Revit workflows',font=font(18),fill='#a4b5cd')
        for j,label in enumerate(['COLLECT','INSPECT','REVIEW']):
            x=38+j*125;d.rounded_rectangle((x,361,x+112,396),radius=7,fill='#214739' if j==phase else '#16283d',outline=TEAL if j==phase else '#30445e')
            d.text((x+12,370),label,font=font(14,True),fill=TEAL if j==phase else '#a4b5cd')
        d.line((36,426,924,426),fill='#30445e')
        d.text((38,442),'Synthetic geometry illustration · not a Revit recording or engineering acceptance result',font=font(16),fill='#a4b5cd')
        frames.append(im)
durations=[130]*len(frames)
for i in (11,23,35):durations[i]=1400
frames[0].save(ASSETS/'coordination-study.gif',save_all=True,append_images=frames[1:],duration=durations,loop=0,optimize=True)
frames[23].save(ASSETS/'coordination-study.png')
print('Built SVG covers, 48-facet STL, fictional CSV, GIF and static diagram.')

