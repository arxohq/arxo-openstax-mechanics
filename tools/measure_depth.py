#!/usr/bin/env python3
"""Reproduce five CNXML depth measurements using the captured common classifier.

Python 3.12, standard library only; no npm runtime, private corpus or full corpus
scan. Model/source hashes are checked before parsing. This adapter collects the
inputs and report; all classification is performed by boundaries.depth.
"""
from pathlib import Path
from collections import Counter
import argparse, hashlib, json, sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools/depth'))
import boundaries

def sha(raw):return 'sha256:'+hashlib.sha256(raw).hexdigest()
def verified(path, expected):
    raw=(ROOT/path).read_bytes()
    if sha(raw)!=expected:raise ValueError('Input hash differs: '+path)
    return raw

def measure():
    pin=json.loads((ROOT/'source-pin.json').read_text())
    inputs={row['path']:row for row in pin['files']}
    rows=[]
    for m in pin['models']:
        if not m['name'].startswith('openstax.'):continue
        irrel=f"registry/package/{m['name']}.lawir.json"
        irpath=ROOT/irrel
        ir=json.loads(verified(irrel,m['hashes']['package']))
        assert ir['package']['name']==m['name'] and ir['package']['version']==m['version']
        assert all(n['package']==m['namespace'] for n in ir['nodes']), 'imports are excluded from depth'
        pubs={n['documentHash']:n for n in ir['nodes'] if n['kind']=='publication'}
        docs=[];aggregate={'module':Counter(),'element':Counter()};seen=set()
        for p in sorted((ROOT/m['path']).glob('sources/**/*.cnxml')):
            rel=p.relative_to(ROOT).as_posix();source=inputs[rel]
            raw=verified(rel,source['sha256']);assert len(raw)==source['size']
            pub=pubs[source['sha256']];seen.add(pub['id'])
            module=boundaries.depth(p,irpath)
            element=boundaries.depth(p,irpath,source_unit='cnxml_element')
            assert len(module['rows'])==1
            for axis,value in [('module',module),('element',element)]:
                aggregate[axis].update(row['level'] for row in value['rows'])
            docs.append({'path':rel,'sourceHash':source['sha256'],'publication':pub['id'],'edition':pub['edition'],
                         'module':module['rows'],'elements':element['rows'],'elementDenominator':len(element['rows']),
                         'moduleUnresolvedAnchors':module['unresolved'],'moduleOtherEditionAnchors':module['otherEdition']})
        assert seen=={p['id'] for p in pubs.values()}, 'every own publication is measured'
        rows.append({'spec':m['spec'],'packageHash':m['hashes']['package'],'status':'measured',
                     'denominator':len(docs),'unit':'CNXML module snapshot','levels':dict(aggregate['module']),
                     'elementDenominator':sum(aggregate['element'].values()),'elementLevels':dict(aggregate['element']),
                     'documents':docs,'ownRules':sum(n['kind']=='rule' for n in ir['nodes']),
                     'ownNormTemplates':sum(n['kind']=='norm_template' for n in ir['nodes']),
                     'capturedFragments':sum(n['kind']=='fragment' for n in ir['nodes']),
                     'unmeasuredPublications':[],'unmeasuredFragments':[]})
    assert len(rows)==5
    return rows

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--check',action='store_true');ap.add_argument('--out',type=Path)
    args=ap.parse_args()
    report=json.loads((ROOT/'reports/formalization-depth.json').read_text())
    for origin,delivered in [('.claude/skills/formalize-act/scripts/boundaries.py','tools/depth/boundaries.py'),
                             ('corpus/tools/lib/act_split.py','tools/depth/corpus/tools/lib/act_split.py')]:
        verified(delivered,report['cnxmlImplementationHashes'][origin])
    rows=measure()
    if args.check:
        assert rows==report['packages'][:5], 'recomputed depth differs from recorded report'
    if args.out:
        args.out.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    for row in rows:
        print(row['spec'],row['levels'].get('EXECUTABLE',0),'/',row['denominator'],'module snapshots;',
              row['elementLevels'].get('EXECUTABLE',0),'/',row['elementDenominator'],'elements')
    print('PASS: five own packages, exact source editions, two structural axes; corpus not_checked')
if __name__=='__main__':main()
