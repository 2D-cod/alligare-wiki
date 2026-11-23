#!/usr/bin/env python3
"""Lint estrutural da wiki (sem LLM). Uso: lint.py [--quiet]
--quiet: imprime SÓ se houver problemas (para cron no_agent)."""
import hashlib, os, re, sys
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAYER2 = ['entities', 'concepts', 'comparisons', 'queries', 'ops']
REQ = ['title', 'created', 'updated', 'type', 'tags', 'sources']
TYPES = {'entity', 'concept', 'comparison', 'query', 'summary'}
quiet = '--quiet' in sys.argv


def fm(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m: return None, text
    d = {}
    for line in m.group(1).splitlines():
        if ':' in line and not line.startswith(' '):
            k, v = line.split(':', 1); d[k.strip()] = v.strip()
    return d, text[m.end():]


schema = open(os.path.join(W, 'SCHEMA.md'), encoding='utf-8').read()
tax = set()
for line in schema.splitlines():
    if line.startswith('TAXONOMY:'):
        tax = {t.strip() for t in line.split(':', 1)[1].split(',') if t.strip()}

pages = {}
for d in LAYER2:
    p = os.path.join(W, d)
    if not os.path.isdir(p): continue
    for f in sorted(os.listdir(p)):
        if f.endswith('.md'):
            pages[f[:-3]] = os.path.join(p, f)
allslugs = set(pages)
for root, _, files in os.walk(W):
    for f in files:
        if f.endswith('.md'): allslugs.add(f[:-3])

issues = {'links quebrados': [], 'órfãs': [], 'fora do índice': [], 'frontmatter': [],
          'tags fora da taxonomia': [], 'poucos links': [], 'longas (>200 linhas)': [], 'raw alterado': [], 'log': []}
inbound = {s: 0 for s in pages}
index = open(os.path.join(W, 'index.md'), encoding='utf-8').read()
for slug, path in pages.items():
    t = open(path, encoding='utf-8').read()
    d, body = fm(t)
    rel = os.path.relpath(path, W)
    if d is None:
        issues['frontmatter'].append(rel + ' (sem frontmatter)'); continue
    miss = [k for k in REQ if k not in d]
    if miss: issues['frontmatter'].append('%s falta %s' % (rel, ','.join(miss)))
    if d.get('type') not in TYPES: issues['frontmatter'].append('%s type inválido' % rel)
    tags = [x.strip() for x in d.get('tags', '').strip('[]').split(',') if x.strip()]
    bad = [x for x in tags if tax and x not in tax]
    if bad: issues['tags fora da taxonomia'].append('%s: %s' % (rel, ','.join(bad)))
    links = set(re.findall(r'\[\[([^\]|#]+)', body))
    if len(links) < 2: issues['poucos links'].append(rel)
    for l in links:
        if l not in allslugs: issues['links quebrados'].append('%s -> [[%s]]' % (rel, l))
        elif l in inbound and l != slug: inbound[l] += 1
    if '[[%s]]' % slug not in index: issues['fora do índice'].append(rel)
    if t.count('\n') > 200: issues['longas (>200 linhas)'].append(rel)
for s, n in inbound.items():
    if n == 0: issues['órfãs'].append(os.path.relpath(pages[s], W))
# raw sha256
for root, _, files in os.walk(os.path.join(W, 'raw')):
    for f in files:
        if not f.endswith('.md'): continue
        t = open(os.path.join(root, f), encoding='utf-8').read()
        d, body = fm(t)
        if d and 'sha256' in d and hashlib.sha256(body.encode()).hexdigest() != d['sha256']:
            issues['raw alterado'].append(os.path.relpath(os.path.join(root, f), W))
lg = open(os.path.join(W, 'log.md'), encoding='utf-8').read()
if len(re.findall(r'^## \[', lg, re.M)) > 500: issues['log'].append('log.md > 500 entradas: rotacionar')
total = sum(len(v) for v in issues.values())
if total == 0:
    if not quiet: print('OK: %d páginas, 0 problemas' % len(pages))
    sys.exit(0)
print('Wiki lint: %d problema(s) em %d páginas' % (total, len(pages)))
for k, v in issues.items():
    if v:
        print('\n## %s (%d)' % (k, len(v)))
        for x in v[:25]: print('- ' + x)
sys.exit(1)
