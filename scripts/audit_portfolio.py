from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "projects"

REQUIRED = [
    "README.md",
    "docs/BUSINESS_IMPACT.md",
    "docs/RESULTS.md",
    "docs/ARCHITECTURE.md",
    "docs/TECHNICAL_DECISIONS.md",
    "docs/DATA.md",
    "docs/SECURITY_AND_PERMISSIONS.md",
    "docs/CREDENTIALS_AND_INTEGRATIONS.md",
    "docs/ENVIRONMENTS.md",
    "docs/LIMITATIONS.md",
    "examples/README.md",
    "technical/README.md",
    "technical/VALIDATION.md",
]

BI_VISUAL_EXCEPTIONS = {
    "sc-14-power-bi-executive-decision-system",
    "sc-15-tableau-commercial-analytics",
}

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_structure(errors: list[str]) -> list[Path]:
    dirs = sorted(p for p in PROJECTS.iterdir() if p.is_dir() and p.name.startswith("sc-"))
    if len(dirs) != 29:
        fail(errors, f"expected 29 project directories, found {len(dirs)}")

    for p in dirs:
        for rel in REQUIRED:
            if not (p / rel).exists():
                fail(errors, f"{p.name}: missing {rel}")

        if p.name not in BI_VISUAL_EXCEPTIONS:
            visual_dir = p / "examples" / "visuals"
            if not visual_dir.exists() or not any(x.is_file() for x in visual_dir.iterdir()):
                fail(errors, f"{p.name}: missing analytical visual evidence")

    return dirs


def validate_json(errors: list[str]) -> None:
    for path in ROOT.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(errors, f"invalid JSON {path.relative_to(ROOT)}: {exc}")


def validate_python(errors: list[str]) -> None:
    for path in ROOT.rglob("*.py"):
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except SyntaxError as exc:
            fail(errors, f"python syntax error {path.relative_to(ROOT)}:{exc.lineno}: {exc.msg}")


def validate_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            target = target.strip().split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("?", 1)[0]
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(errors, f"link escapes repository in {path.relative_to(ROOT)}: {target}")
                continue
            if not resolved.exists():
                fail(errors, f"broken local link in {path.relative_to(ROOT)}: {target}")


def validate_secrets(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() in {".pem", ".p12", ".pfx"} or path.name.endswith(".key"):
            fail(errors, f"private-key-like file tracked: {path.relative_to(ROOT)}")
            continue
        if path.stat().st_size > 2_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(errors, f"secret-like token found in {path.relative_to(ROOT)}")


def validate_catalog(errors: list[str], dirs: list[Path]) -> None:
    projects_md = (ROOT / "PROJECTS.md").read_text(encoding="utf-8")
    tech_md = (ROOT / "TECHNOLOGIES.md").read_text(encoding="utf-8")
    for p in dirs:
        project_id = p.name.split("-", 2)[:2]
        project_id = "-".join(project_id).upper()
        if project_id not in projects_md:
            fail(errors, f"{project_id} missing from PROJECTS.md")
        if not (ROOT / "catalog" / f"{p.name}.yml").exists():
            fail(errors, f"{p.name}: missing individual catalog entry")
    if "# Technology index" not in tech_md:
        fail(errors, "TECHNOLOGIES.md missing expected heading")


def run_stdlib_examples(errors: list[str], dirs: list[Path]) -> None:
    for p in dirs:
        main = p / "technical" / "src" / "main.py"
        if not main.exists():
            continue

        source = main.read_text(encoding="utf-8")
        third_party_markers = [
            "import pandas", "from pandas", "import numpy", "from numpy",
            "import fastapi", "from fastapi", "import sklearn", "from sklearn",
            "import xgboost", "from xgboost", "import shap", "from shap",
            "import streamlit", "from streamlit", "import cvxpy", "from cvxpy",
            "import ortools", "from ortools", "import simpy", "from simpy",
        ]
        if any(marker in source for marker in third_party_markers):
            continue

        try:
            subprocess.run(
                [sys.executable, str(main)],
                cwd=p / "technical",
                check=True,
                capture_output=True,
                text=True,
                timeout=20,
            )
        except Exception as exc:
            fail(errors, f"{p.name}: deterministic main.py failed: {exc}")


def main() -> int:
    errors: list[str] = []
    dirs = validate_structure(errors)
    validate_json(errors)
    validate_python(errors)
    validate_links(errors)
    validate_secrets(errors)
    validate_catalog(errors, dirs)
    run_stdlib_examples(errors, dirs)

    if errors:
        print("PORTFOLIO AUDIT FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Portfolio audit passed: {len(dirs)} projects")
    print("Power BI and Tableau are allowed to omit native visual evidence until supplied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
