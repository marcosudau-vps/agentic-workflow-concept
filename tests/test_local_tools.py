"""Standard-library tests for structural validators and prompt rendering."""
from __future__ import annotations
import importlib.util
from pathlib import Path
import sys
import tempfile
import json
import unittest

ROOT=Path(__file__).resolve().parents[1]
SCRIPTS=ROOT/'03_ANWENDUNGSEBENE'/'SKRIPTE'

def load(name):
    spec=importlib.util.spec_from_file_location(name,SCRIPTS/(name+'.py'))
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

render=load('render_prompt')
project=load('check_project_records')
repo=load('check_repository')

class LocalTools(unittest.TestCase):
    def test_prompt_render(self):
        self.assertEqual(render.render('X {{AP_ID}}',{'AP_ID':'AP-001'}),'X AP-001')
        with self.assertRaises(ValueError):render.render('X {{AP_ID}}',{})
        with self.assertRaises(ValueError):render.render('X {{AP_ID}}',{'AP_ID':' '})
    def test_repository(self):
        self.assertEqual([],repo.check())
    def test_project_bad_phase(self):
        sample=ROOT/'03_ANWENDUNGSEBENE'/'VORLAGEN'
        with tempfile.TemporaryDirectory() as td:
            target=Path(td)
            (target/'TRACKING').mkdir();(target/'20_PLANUNG'/'TRACEABILITY').mkdir(parents=True);(target/'20_PLANUNG'/'EVIDENCE').mkdir(parents=True)
            targets={
              'TRACKING/WORKFLOW_STATUS.json':'TRACKING/WORKFLOW_STATUS.json',
              '20_PLANUNG/PLAN_STATUS.json':'PLANUNG/PLAN_STATUS.json',
              '20_PLANUNG/TRACEABILITY/requirements.json':'PLANUNG/TRACEABILITY/requirements.json',
              '20_PLANUNG/EVIDENCE/package-manifest.json':'PLANUNG/EVIDENCE/package-manifest.json'}
            for dest,source in targets.items(): (target/dest).write_bytes((sample/source).read_bytes())
            wf=target/'TRACKING/WORKFLOW_STATUS.json';data=json.loads(wf.read_text(encoding='utf-8'))
            data['workflowPhase']='READY_FOR_IMPLEMENTATION'
            wf.write_text(json.dumps(data),encoding='utf-8')
            self.assertTrue(any('implementation may not be ready' in x for x in project.check_project(target)))
            data['workflowPhase']='BLOCKED'
            wf.write_text(json.dumps(data),encoding='utf-8')
            self.assertEqual([],project.check_project(target))

if __name__=='__main__':unittest.main()
