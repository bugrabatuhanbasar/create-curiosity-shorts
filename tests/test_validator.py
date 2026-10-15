import copy
import importlib.util
import unittest
from pathlib import Path

root=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('validator',root/'skills/create-curiosity-shorts/scripts/validate_package.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

def fixture():
    return {'status':'PLANNED','target_seconds':10,'narration':'This example contains a short factual explanation.',
        'words_per_minute':145,'pause_seconds':1,
        'scenes':[{'id':'S01','start':0,'end':4,'voice_text':'This example','visual':'Show the identified object close up','material_ids':['M01']},
                  {'id':'S02','start':4,'end':10,'voice_text':'contains a short factual explanation.','visual':'Show a labeled original diagram','material_ids':['M02']}],
        'materials':[{'id':'M01','availability':'search-only','rights_status':'unknown','planned_ai_attempts':0},
                     {'id':'M02','availability':'planned','rights_status':'original','planned_ai_attempts':0}],
        'claims':[{'id':'I01','status':'supplied-unverified','source_ids':[]}],
        'sources':[],'production_tasks':[{'id':'T01','min_minutes':10,'max_minutes':20}],
        'constraints':{'production_minutes':30,'ai_attempts':0},'audit':[]}

class Validation(unittest.TestCase):
    def test_valid(self):self.assertEqual(module.validate(fixture()),[])
    def test_overlap(self):
        x=fixture();x['scenes'][1]['start']=3;self.assertTrue(module.validate(x))
    def test_gap(self):
        x=fixture();x['scenes'][1]['start']=5;self.assertTrue(module.validate(x))
    def test_total(self):
        x=fixture();x['target_seconds']=12;self.assertTrue(module.validate(x))
    def test_unknown_asset(self):
        x=fixture();x['scenes'][0]['material_ids']=['M99'];self.assertTrue(module.validate(x))
    def test_speech(self):
        x=fixture();x['narration']='word '*100;self.assertTrue(module.validate(x))
    def test_ai_cap(self):
        x=fixture();x['materials'][0]['planned_ai_attempts']=1;self.assertTrue(module.validate(x))
    def test_workload(self):
        x=fixture();x['constraints']['production_minutes']=5;self.assertTrue(module.validate(x))
    def test_unjustified_ready(self):
        x=fixture();x['status']='EDIT READY';self.assertTrue(module.validate(x))
    def test_verified_without_source(self):
        x=fixture();x['claims'][0]['status']='verified';self.assertTrue(module.validate(x))
    def test_duplicate(self):
        x=fixture();x['materials'].append(copy.deepcopy(x['materials'][0]));self.assertTrue(module.validate(x))
    def test_malformed(self):
        for x in [None,[],{}, {'status':'PLANNED'}]:self.assertTrue(module.validate(x))
    def test_nan(self):
        x=fixture();x['scenes'][0]['start']=float('nan');self.assertTrue(module.validate(x))
    def test_bad_material_refs(self):
        x=fixture();x['scenes'][0]['material_ids']=[{}];self.assertTrue(module.validate(x))

if __name__=='__main__':unittest.main()
