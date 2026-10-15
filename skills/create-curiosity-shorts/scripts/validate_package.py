#!/usr/bin/env python3
"""Check production summary structure/timing. No API, network or dependencies."""
import argparse,json,math,sys
from pathlib import Path

def number(x):
    return isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x)

def validate(p):
    errors=[]
    if not isinstance(p,dict):return ['Package must be an object']
    required=['status','target_seconds','narration','words_per_minute','pause_seconds','scenes','materials','claims','sources','production_tasks','constraints','audit']
    for k in required:
        if k not in p:errors.append('Missing '+k)
    if errors:return errors
    if p['status'] not in ['PROVISIONAL','PLANNED','EDIT READY']:errors.append('Invalid status')
    if not number(p['target_seconds']) or p['target_seconds']<=0:errors.append('Invalid target_seconds')
    if not isinstance(p['narration'],str) or not p['narration'].strip():errors.append('Empty narration')
    if not number(p['words_per_minute']) or p['words_per_minute']<=0:errors.append('Invalid words_per_minute')
    if not number(p['pause_seconds']) or p['pause_seconds']<0:errors.append('Invalid pause_seconds')
    for k in ['scenes','materials','claims','sources','production_tasks','audit']:
        if not isinstance(p[k],list):errors.append(k+' must be an array')
    if not isinstance(p['constraints'],dict):errors.append('constraints must be object')
    if errors:return errors
    def ids(items,label):
        seen=set()
        for x in items:
            if not isinstance(x,dict) or not isinstance(x.get('id'),str) or not x['id']:errors.append('Missing '+label+' id');continue
            if x['id'] in seen:errors.append('Duplicate '+label+' id '+x['id'])
            seen.add(x['id'])
        return seen
    mids=ids(p['materials'],'material');ids(p['scenes'],'scene');sids=ids(p['sources'],'source');ids(p['claims'],'claim')
    if not p['scenes']:errors.append('No scenes')
    cursor=0
    for s in p['scenes']:
        if not isinstance(s,dict):continue
        a,b=s.get('start'),s.get('end')
        if not number(a) or not number(b) or b<=a or a<0:errors.append('Invalid scene interval');continue
        if abs(a-cursor)>.02:errors.append('Scene gap or overlap at '+s.get('id','?'))
        cursor=b
        if not isinstance(s.get('voice_text'),str):errors.append('Missing voice_text')
        if not isinstance(s.get('visual'),str) or not s.get('visual','').strip():errors.append('Missing concrete visual')
        refs=s.get('material_ids')
        if not isinstance(refs,list):errors.append('Missing material_ids')
        elif any(not isinstance(x,str) or x not in mids for x in refs):errors.append('Unknown material reference')
    if abs(cursor-p['target_seconds'])>.02:errors.append('Scene total differs from target')
    speech=len(p['narration'].split())/p['words_per_minute']*60+p['pause_seconds']
    if speech>p['target_seconds']+.1:errors.append('Narration estimate exceeds timeline')
    for c in p['claims']:
        if not isinstance(c,dict):continue
        if c.get('status')=='verified' and not c.get('source_ids'):errors.append('Verified claim lacks source')
        refs=c.get('source_ids',[])
        if not isinstance(refs,list) or any(not isinstance(x,str) or x not in sids for x in refs):errors.append('Unknown claim source')
    if p['status']=='EDIT READY':
        if not p['claims'] or any(c.get('status')!='verified' for c in p['claims'] if isinstance(c,dict)):errors.append('Edit ready requires verified claims')
        if any(m.get('availability')!='acquired' or m.get('rights_status')!='recorded' for m in p['materials'] if isinstance(m,dict)):errors.append('Edit ready requires acquired/rights-recorded materials')
        if p.get('timing_status')!='measured':errors.append('Edit ready requires measured timing')
    low=high=0
    for task in p['production_tasks']:
        if not isinstance(task,dict):errors.append('Invalid task');continue
        a,b=task.get('min_minutes'),task.get('max_minutes')
        if not number(a) or not number(b) or a<0 or b<a:errors.append('Invalid production time range');continue
        low+=a;high+=b
    cap=p['constraints'].get('production_minutes')
    if cap is not None:
        if not number(cap) or cap<0:errors.append('Invalid production cap')
        elif high>cap:errors.append('Production high estimate exceeds cap')
    attempts=0
    for m in p['materials']:
        if not isinstance(m,dict):continue
        v=m.get('planned_ai_attempts',0)
        if not isinstance(v,int) or isinstance(v,bool) or v<0:errors.append('Invalid AI attempt count')
        else:attempts+=v
    cap=p['constraints'].get('ai_attempts')
    if cap is not None:
        if not isinstance(cap,int) or isinstance(cap,bool) or cap<0:errors.append('Invalid AI cap')
        elif attempts>cap:errors.append('AI attempt cap exceeded')
    return errors

def main():
    a=argparse.ArgumentParser();a.add_argument('file',type=Path);args=a.parse_args()
    try:p=json.loads(args.file.read_text(encoding='utf-8'));errors=validate(p)
    except (OSError,ValueError,TypeError) as e:print(json.dumps({'ok':False,'errors':[str(e)]}));return 1
    print(json.dumps({'ok':not errors,'errors':errors,'scope':'Structure and arithmetic only; factual and editorial review still required'},ensure_ascii=False,indent=2))
    return int(bool(errors))
if __name__=='__main__':sys.exit(main())
