"""Check generated page metadata, internal targets, schema and sitemap."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1]/'public'
errors=[];count=0
class Page(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=set();self.h1=0;self.canonical=0;self.description=0;self.in_json=False;self.data='';self.schemas=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1':self.h1+=1
        if 'id' in a:self.ids.add(a['id'])
        if tag=='link' and a.get('rel')=='canonical':self.canonical+=1
        if tag=='meta' and a.get('name')=='description':self.description+=1
        for key in ['href','src']:
            if key in a:self.links.append(a[key])
        if tag=='script' and a.get('type')=='application/ld+json':self.in_json=True;self.data=''
    def handle_data(self,data):
        if self.in_json:self.data+=data
    def handle_endtag(self,tag):
        if tag=='script' and self.in_json:self.schemas.append(json.loads(self.data));self.in_json=False
for path in root.rglob('*.html'):
    count+=1;p=Page();p.feed(path.read_text())
    if (p.h1,p.canonical,p.description)!=(1,1,1):errors.append(f'{path}: metadata/headings')
    if not p.schemas:errors.append(f'{path}: schema missing')
    for link in p.links:
        u=urlsplit(link)
        if u.scheme or u.netloc:continue
        target=root/unquote(u.path.lstrip('/')) if u.path.startswith('/') else path.parent/unquote(u.path)
        if not u.path:target=path
        if target.is_dir():target=target/'index.html'
        if not target.exists():errors.append(f'{path}: broken internal link {link}')
        elif u.fragment and target.suffix=='.html':
            q=Page();q.feed(target.read_text())
            if u.fragment not in q.ids:errors.append(f'{path}: missing fragment {link}')
ET.parse(root/'sitemap.xml')
guides=json.loads((root.parent/'content/guides.json').read_text())
assert len(guides)==10
for g in guides:
    words=sum(len(t.split()) for h,t in g['sections'])
    if words<400:errors.append(f'{g["slug"]}: only {words} words')
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: {count} HTML pages; internal links, fragments, headings, metadata, JSON-LD, sitemap; 10 guides with 400+ body words each.')
