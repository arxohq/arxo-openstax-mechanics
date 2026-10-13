#!/usr/bin/env python3
"""Verify this selected consumer archive; never discover the full corpus."""
import argparse, hashlib, json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(path):return json.loads((ROOT/path).read_text())
def check_expectations(result, expectations):
 q=result['results'][0]; fields={'result_kind':'resultKind','truth_status':'truthStatus','evaluation_status':'evaluationStatus'}
 for ex in expectations:
  if 'field' in ex:
   assert ex['op']=='eq' and ex['field'] in fields,ex
   assert q[fields[ex['field']]]==ex['value'],ex
  elif ex.get('observation')=='applied':
   found=any(n.get('rule')==ex['value'] for n in result['proofGraph']['nodes']);assert found != ex.get('negated',False),ex
  else:raise AssertionError('Unchecked expectation: '+str(ex))
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--law',default='law');ap.add_argument('--packages',action='store_true');args=ap.parse_args()
 for name in ['source-pin.json','CANON-MANIFEST.json']:
  for row in read(name)['files']:
   raw=(ROOT/row['path']).read_bytes();assert len(raw)==row['size'],row['path'];assert 'sha256:'+hashlib.sha256(raw).hexdigest()==row['sha256'],row['path']
 for m in read('source-pin.json')['models']:
  for flavor,h in m['hashes'].items():
   raw=(ROOT/f"registry/{flavor}/{m['name']}.lawir.json").read_bytes();assert 'sha256:'+hashlib.sha256(raw).hexdigest()==h
   ir=json.loads(raw);assert ir['package']['name']==m['name'];assert ir['package']['version']==m['version']
  own=read(f"registry/package/{m['name']}.lawir.json");assert all(n['package']==m['namespace'] for n in own['nodes'])
 for row in read('examples/index.json'):
  folder=ROOT/'examples'/row['name'];expected=json.loads((folder/'result.json').read_text());check_expectations(expected,row['expectations'])
  ir=json.loads((folder/'request.json').read_text())['ir'];nodes={n['id']:n for n in ir['nodes']}
  for ex in row['expectations']:
   if ex.get('observation')=='applied' and not ex.get('negated'):
    rule=nodes[ex['value']];assert rule.get('anchors'),ex['value']
    for anchor in rule['anchors']:assert anchor in nodes and nodes[anchor]['kind']=='fragment',anchor
  for _ in range(2):
   actual=json.loads(subprocess.check_output([args.law,'eval',str(folder)],text=True));assert actual==expected,row['name']
  print('REPLAY PASS',row['name'],expected['resultHash'])
 sample=ROOT/'examples/friction-at-limit/result.json';summary=json.loads(subprocess.check_output([args.law,'inspect',str(sample),'summary'],text=True));assert summary['ok']
 tree=json.loads(subprocess.check_output([args.law,'engine','unfold',str(ROOT/'registry/world/openstax.dynamics.lawir.json'),'stays_at_rest','--clir',str(ROOT/'registry/package'),'--depth','2','--lang','en','--json'],text=True));assert tree==read('reports/unfold-friction.json')
 if args.packages:
  for row in read('reports/targeted-package-checks.json')['packages']:
   if row['status']=='no_declared_scenarios':continue
   name=row['spec'].split('@')[0];doc=json.loads(subprocess.check_output([args.law,'test',str(ROOT/'packages'/name),'--file',row['suite'],'--json'],text=True));assert doc.get('failed',0)==0,doc
   print('NATIVE SUITE PASS',name,doc['total'])
 print('PASS: 8 pinned models; 12 native examples twice; inspect and source-anchored unfold; corpus not_checked')
if __name__=='__main__':main()
