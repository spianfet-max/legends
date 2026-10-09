import re, json, sys, os
root = sys.argv[1]
readme = open(os.path.join(root, 'README.md'), encoding='utf-8').read()
rows = re.findall(r'^\| \[`([^`]+)`\]\([^)]*\)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$', readme, re.M)
CAT = {
 'value': ['buffett','munger','graham-net-net','schloss-cigar-butt','klarman-deep-value','li-lu-value','templeton-max-pessimism','hohn-concentrated-quality','nick-sleep-scale-economies','watsa-insurance-float','duanyongping-benfen-value','qiuguolu-value-quality','danbin-longterm-compounder','zhanglei-longterm-research-value','fengliu-reverse-weakhand'],
 'growth': ['lynch-growth','oneil-canslim','coleman-tiger-growth','cathie-wood-innovation','serenity','sequoia-founder-market','a16z-techno-optimist','usv-network-effects','founders-fund-contrarian','yc-early-pmf'],
 'trend': ['livermore','darvas-box','minervini-vcp','seykota-systematic-trend','turtle-trading','simons-quant','tangnengtong-shortterm-ta','chenhao-limit-up'],
 'macro': ['soros-reflexivity','druckenmiller','marks-cycles','ptj-macro-trend','dalio-principles-allweather','gundlach-bonds','tepper-distressed-macro','libei-macro-hedge','shihanbing-macro-interest-analysis','dengxiaofeng-cycle-industry'],
 'activist': ['icahn-activist','ackman-concentrated-activism','greenblatt-special-situations','burry-asymmetric-contrarian'],
 'short': ['einhorn-forensic-short','muddy-waters-forensic','hindenburg-investigation','spruce-point-accounting-short'],
 'crypto': ['ansem-crypto','arthur-hayes-liquidity','hsaka-crypto-ta','cryptocred-structure','willy-woo-onchain','cobie-cycle-filter','paradigm-crypto-research','multicoin-thesis-vc','a16z-crypto','delphi-thematic-crypto','placeholder-token-networks','grayscale-crypto-sectors'],
}
cat_of = {s:c for c,l in CAT.items() for s in l}
DROP = {'Questflow Use','YouTube','Source Notes','Reading List','Podcasts','Canonical Cases'}
def strip(md):
    parts = re.split(r'(?m)^(?=## )', md)
    keep = [p for p in parts if not (p.startswith('## ') and p[3:].split('\n')[0].strip() in DROP)]
    return re.sub(r'\n{3,}', '\n\n', ''.join(keep)).strip()
out = []
for slug, investor, model in rows:
    d = os.path.join(root, 'skills', slug)
    sk = os.path.join(d, 'SKILL.md'); iv = os.path.join(d, 'invest.md')
    if not os.path.exists(sk): continue
    skill = strip(open(sk, encoding='utf-8').read())
    inv = strip(open(iv, encoding='utf-8').read()) if os.path.exists(iv) else ''
    title = re.search(r'(?m)^# (.+)$', skill)
    out.append(dict(slug=slug, investor=investor.strip(), model=model.strip(), cat=cat_of.get(slug,'other'),
                    title=title.group(1).strip() if title else slug, skill=skill, invest=inv))
missing = [s for s in os.listdir(os.path.join(root,'skills')) if s not in {o['slug'] for o in out}]
print(len(out), 'skills; uncategorised:', [o['slug'] for o in out if o['cat']=='other'], 'missing:', missing, file=sys.stderr)
print(sum(len(o['skill'])+len(o['invest']) for o in out), 'chars', file=sys.stderr)
json.dump(out, open(sys.argv[2],'w',encoding='utf-8'), ensure_ascii=False)
