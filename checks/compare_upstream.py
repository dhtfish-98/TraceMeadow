"""Compare deterministic observations with a pinned upstream checkout."""
import argparse as audit_argparse
import json as audit_json
from pathlib import Path as AuditPath
import subprocess as audit_subprocess
import sys as audit_sys

audit_parser=audit_argparse.ArgumentParser()
audit_parser.add_argument('--upstream-root',type=AuditPath,required=True)
audit_options=audit_parser.parse_args()
audit_project='TraceMeadow'
audit_root=AuditPath(__file__).resolve().parents[1]
audit_observer=audit_root/'checks/differential_observer.py'
audit_observations=[]
for audit_variant,audit_location in [('original',audit_options.upstream_root.resolve()),('derivative',audit_root)]:
    audit_command=[audit_sys.executable,str(audit_observer),audit_project,audit_variant,str(audit_location)]
    if audit_project=='ImageQuay':audit_command.extend(['--fixtures',str(audit_root/'checks/bins')])
    audit_result=audit_subprocess.run(audit_command,text=True,capture_output=True,check=True)
    audit_observations.append(audit_json.loads(audit_result.stdout))
audit_old,audit_new=audit_observations
assert len(audit_old)==len(audit_new),(len(audit_old),len(audit_new))
for cases in (audit_old,audit_new):
    added=[row for row in cases if row[0][0] in ('aggregation-owned','callstack-owned')]
    assert len(added)==100
    for row in added:
        assert row[1]=='return' and row[2],row
        if row[0][0]=='callstack-owned':
            assert len(row[2])==1 and len(row[2][0]['frames'])==40,row
audit_differences=[]
audit_changed_errors=0
for i,(old,new) in enumerate(zip(audit_old,audit_new)):
    if old[0]==new[0] and old[0][0]=='stream-boundary':
        assert old[1:3]==['exception','KeyError'],old
        assert new[1:3]==['exception','TraceFormatError'],new
        expected=('trace version: truncated data at byte '+str(new[0][1])) if new[0][1]<4 else 'unsupported trace version'
        assert new[3]==expected,new
        audit_changed_errors+=1
    elif old!=new:
        audit_differences.append({'index':i,'old':old,'new':new})
assert audit_changed_errors==60

if audit_differences:
    print(audit_json.dumps(audit_differences[:10],ensure_ascii=False,indent=2))
    raise SystemExit(1)
print(audit_json.dumps({'project':audit_project,'observations':len(audit_old),'equal_observations':len(audit_old)-audit_changed_errors,'intentional_checked_error_changes':audit_changed_errors,'mismatches':0,'status':'PASS'}))
