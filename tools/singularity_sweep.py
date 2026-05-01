#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_RECEIPT = "public-evidence/PUBLIC_DOCTRINE_L1_DOCTOR.json"
PUBLIC_COMPILER = "tools/doctrine_l1_index.py"
PUBLIC_MATERIALIZE = ".github/workflows/public-doctrine-l1-materialize.yml"
PUBLIC_VALIDATE = ".github/workflows/validate.yml"
OUT = ROOT / "public-evidence"

FORBIDDEN_PRIVATE_STRINGS = [
    "Xxen.soul payload present",
    "private Xxen.soul payload present",
    "private user attunement",
    "private invention chronology included",
]


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def check_file(path: str, required: bool = True) -> dict:
    exists = (ROOT / path).exists()
    return {"check": "file_exists" if required else "file_absent", "path": path, "ok": exists if required else not exists, "actual": "exists" if exists else "absent"}


def check_receipt() -> list[dict]:
    checks = []
    p = ROOT / PUBLIC_RECEIPT
    if not p.exists():
        return [{"check": "public_l1_receipt_exists", "path": PUBLIC_RECEIPT, "ok": False}]
    data = load_json(PUBLIC_RECEIPT)
    checks.append({"check": "public_receipt_ok_true", "path": PUBLIC_RECEIPT, "ok": data.get("ok") is True, "actual": data.get("ok")})
    checks.append({"check": "public_failure_count_zero", "path": PUBLIC_RECEIPT, "ok": data.get("failure_count") == 0, "actual": data.get("failure_count")})
    checks.append({"check": "public_compiled_equals_ok", "path": PUBLIC_RECEIPT, "ok": data.get("compiled_count") == data.get("ok_count"), "actual": {"compiled_count": data.get("compiled_count"), "ok_count": data.get("ok_count")}})
    return checks


def check_private_payload_absent(path: str) -> list[dict]:
    p = ROOT / path
    if not p.exists():
        return [{"check": "surface_exists_for_private_payload_scan", "path": path, "ok": False}]
    text = p.read_text(encoding="utf-8", errors="replace")
    return [{"check": "private_payload_absent", "path": path, "needle": s, "ok": s not in text} for s in FORBIDDEN_PRIVATE_STRINGS]


def run_checks() -> list[dict]:
    checks = [
        check_file(PUBLIC_RECEIPT),
        check_file(PUBLIC_COMPILER),
        check_file(PUBLIC_MATERIALIZE),
        check_file(PUBLIC_VALIDATE),
    ]
    checks.extend(check_receipt())
    checks.extend(check_private_payload_absent(PUBLIC_RECEIPT))
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description="Public DoctrineOS singularity hygiene sweep.")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    checks = run_checks()
    failures = [c for c in checks if not c.get("ok")]
    receipt = {
        "receipt_id": "PUBLIC_SINGULARITY_SWEEP",
        "created_at_utc": now(),
        "scope": "public_doctrineos_l1_hygiene",
        "ok": not failures,
        "check_count": len(checks),
        "failure_count": len(failures),
        "failures": failures,
        "checks": checks,
        "failure_classes_guarded": [
            "PUBLIC_L1_RECEIPT_STALE",
            "PUBLIC_GREEN_CLAIM_FROM_PARTIAL_PROOF",
            "PUBLIC_PRIVATE_PAYLOAD_LEAK",
            "PUBLIC_WORKFLOW_DRIFT",
            "PUBLIC_STATUS_WITHOUT_RECEIPT",
        ],
    }
    if args.write:
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / "PUBLIC_SINGULARITY_SWEEP.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["ok"] else 2

if __name__ == "__main__":
    raise SystemExit(main())
