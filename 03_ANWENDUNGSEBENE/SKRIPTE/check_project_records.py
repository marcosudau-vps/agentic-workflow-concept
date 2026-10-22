#!/usr/bin/env python3
"""Offline structural project checker. No approvals, remote calls or runtime tests."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

WF = {'READY_FOR_IMPLEMENTATION','IMPLEMENTATION_IN_PROGRESS','REVIEW_READY','REVIEW_IN_PROGRESS','CHANGES_REQUIRED','CORRECTION_IN_PROGRESS','WAITING_FOR_APPROVAL','READY_FOR_CANONICALIZATION','CANONICALIZED','SERVER_FIX_REQUIRED','BLOCKED','SUPERSEDED','COMPLETED'}
PLAN = {'PLANNING_IN_PROGRESS','PLAN_HARDENING','PLAN_CHANGES_REQUIRED','PLAN_REVIEW_READY','PLAN_ROOT_PASS','PLAN_WAITING_FOR_APPROVAL','PLAN_APPROVED','BLOCKED'}

def check_project(project: Path) -> list[str]:
    errors=[]
    root=Path(project)
    paths={
        'workflow':root/'TRACKING/WORKFLOW_STATUS.json',
        'plan':root/'20_PLANUNG/PLAN_STATUS.json',
        'requirements':root/'20_PLANUNG/TRACEABILITY/requirements.json',
        'manifest':root/'20_PLANUNG/EVIDENCE/package-manifest.json',
    }
    d={}
    for key,file in paths.items():
        try: d[key]=json.loads(file.read_text(encoding='utf-8'))
        except (OSError,json.JSONDecodeError) as e:errors.append(f'{key}: {e}')
    if len(d)<4:return errors
    wf,plan,req,man = (d[k] for k in ('workflow','plan','requirements','manifest'))
    for key,obj in d.items():
        if not isinstance(obj,dict) or obj.get('schemaVersion')!=1:errors.append(f'{key}: schemaVersion=1 / JSON object required')
    if wf.get('workflowPhase') not in WF:errors.append('workflow: unknown phase')
    if plan.get('workflowPhase') not in PLAN:errors.append('plan: unknown phase')
    if not wf.get('repository') or wf.get('repository')!=plan.get('repository'):errors.append('workflow/plan: repository mismatch')
    if not isinstance(wf.get('openFindingIds'),list) or not isinstance(plan.get('openFindingIds'),list):errors.append('finding ids must be arrays')
    if not wf.get('nextAction') or not plan.get('nextAction'):errors.append('missing nextAction')
    if wf.get('workflowPhase')=='READY_FOR_IMPLEMENTATION' and plan.get('workflowPhase')!='PLAN_APPROVED':
        errors.append('implementation may not be ready while plan is not approved')
    if wf.get('workflowPhase') in ('WAITING_FOR_APPROVAL','READY_FOR_CANONICALIZATION') and not wf.get('reviewReport'):
        errors.append('review report missing for canonicalization phase')
    if wf.get('workflowPhase')=='READY_FOR_CANONICALIZATION' and not wf.get('humanApproval'):
        errors.append('human approval missing for canonicalization phase')
    if wf.get('workflowPhase')=='CANONICALIZED' and not wf.get('canonicalParent'):
        errors.append('canonical parent missing')
    feature_file=root/'TRACKING/FEATURE_STATUS.json'
    if feature_file.is_file():
        try:
            feature=json.loads(feature_file.read_text(encoding='utf-8'))
            feature_phases={'FEATURE_IN_PROGRESS','FEATURE_REVIEW_READY','FEATURE_REVIEW_IN_PROGRESS','FEATURE_CHANGES_REQUIRED','FEATURE_WAITING_FOR_APPROVAL','FEATURE_READY_FOR_CANONICALIZATION','FEATURE_CANONICALIZED','FEATURE_BLOCKED'}
            if feature.get('workflowPhase') not in feature_phases:errors.append('feature: invalid phase')
            if feature.get('workflowPhase')=='FEATURE_READY_FOR_CANONICALIZATION' and (not feature.get('humanApproval') or not feature.get('reviewReport')):
                errors.append('feature: human approval / independent review missing')
        except (OSError,json.JSONDecodeError) as exc:errors.append(f'feature: {exc}')
    packages=man.get('packages',[])
    if not isinstance(packages,list):errors.append('manifest packages not a list');packages=[]
    ids=[p.get('id') for p in packages if isinstance(p,dict)]
    if len(ids)!=len(set(ids)):errors.append('duplicate package ids')
    reqs=req.get('requirements',[])
    if not isinstance(reqs,list):errors.append('requirements not a list');reqs=[]
    reqids=[r.get('id') for r in reqs if isinstance(r,dict)]
    if len(reqids)!=len(set(reqids)):errors.append('duplicate requirement ids')
    for r in reqs:
        if not isinstance(r,dict):errors.append('requirement not object');continue
        if r.get('ownerPackage') not in ids:errors.append(f"{r.get('id')}: unknown package owner")
        if not r.get('verification'):errors.append(f"{r.get('id')}: verification missing")
    for p in packages:
        if not isinstance(p,dict):continue
        for dep in p.get('dependsOn',[]):
            if dep not in ids:errors.append(f"{p.get('id')}: unknown dependency {dep}")
    return errors

def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--project',type=Path,required=True,help='directory containing TRACKING/ and 20_PLANUNG/')
    args=parser.parse_args()
    errors=check_project(args.project)
    for msg in errors:print('FEHLER:',msg)
    print('Strukturprüfung:', 'FAIL' if errors else 'PASS (nur Struktur, keine fachliche Freigabe)')
    raise SystemExit(bool(errors))
if __name__=='__main__':main()
