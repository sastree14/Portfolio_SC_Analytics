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
    "examples/visuals/result.svg",
    "technical/README.md",
    "technical/VALIDATION.md",
]

ENTRYPOINTS = {
    "sc-04-ai-receptionist-lead-qualification": "technical/run_project.ts",
    "sc-07-full-stack-llm-business-copilot": "technical/run_project.ts",
    "sc-13-r-shiny-forecasting-scenario-planning": "technical/run_project.R",
}

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FONT_RE = re.compile(r'font-size="([0-9.]+)"')
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def entrypoint(project: Path) -> Path:
    rel = ENTRYPOINTS.get(project.name, "technical/run_project.py")
    return project / rel


def validate_structure(errors: list[str]) -> list[Path]:
    dirs = sorted(p for p in PROJECTS.iterdir() if p.is_dir() and p.name.startswith("sc-"))
    if len(dirs) != 32:
        fail(errors, f"expected 32 project directories, found {len(dirs)}")

    for project in dirs:
        for rel in REQUIRED:
            if not (project / rel).exists():
                fail(errors, f"{project.name}: missing {rel}")

        ep = entrypoint(project)
        if not ep.exists():
            fail(errors, f"{project.name}: missing principal entrypoint {ep.relative_to(project)}")

        project_readme = (project / "README.md").read_text(encoding="utf-8")
        tech_readme = (project / "technical" / "README.md").read_text(encoding="utf-8")
        if ep.name not in project_readme:
            fail(errors, f"{project.name}: project README does not expose {ep.name}")
        if ep.name not in tech_readme:
            fail(errors, f"{project.name}: technical README does not expose {ep.name}")
        if "↓\\n" in project_readme:
            fail(errors, f"{project.name}: README contains literal escaped newline in flow diagram")

    return dirs


def validate_visuals(errors: list[str], dirs: list[Path]) -> None:
    for project in dirs:
        path = project / "examples" / "visuals" / "result.svg"
        text = path.read_text(encoding="utf-8")
        if "<svg" not in text:
            fail(errors, f"{project.name}: visual is not SVG")
        if 'width="1200"' not in text or 'height="720"' not in text:
            fail(errors, f"{project.name}: visual should use 1200x720 technical canvas")
        sizes = [float(x) for x in FONT_RE.findall(text)]
        if sizes and max(sizes) > 28:
            fail(errors, f"{project.name}: oversized visual typography ({max(sizes)}px)")
        if len(text) < 1500:
            fail(errors, f"{project.name}: visual appears too sparse to be useful")


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
            resolved = (path.parent / target.split("?", 1)[0]).resolve()
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


def validate_manifests(errors: list[str], dirs: list[Path]) -> None:
    catalog = ROOT / "catalog"
    index = (catalog / "projects.yml").read_text(encoding="utf-8")
    required_markers = [
        "schema_version: 2",
        "project_type: public-portfolio-implementation",
        "designed_for:",
        "why_it_matters:",
        "provenance:",
        "client_claim_allowed: false",
        "evidence:",
        "visuals:",
        "execution:",
    ]
    for project in dirs:
        manifest = catalog / f"{project.name}.yml"
        if not manifest.exists():
            fail(errors, f"{project.name}: missing v2 project manifest")
            continue
        text = manifest.read_text(encoding="utf-8")
        for marker in required_markers:
            if marker not in text:
                fail(errors, f"{project.name}: manifest missing {marker}")
        if f"catalog/{project.name}.yml" not in index:
            fail(errors, f"{project.name}: manifest missing from catalog/projects.yml")


def validate_indexes(errors: list[str], dirs: list[Path]) -> None:
    projects_md = (ROOT / "PROJECTS.md").read_text(encoding="utf-8")
    visuals_md = (ROOT / "VISUALS.md").read_text(encoding="utf-8")
    execution_md = (ROOT / "EXECUTION.md").read_text(encoding="utf-8")

    for project in dirs:
        project_id = "-".join(project.name.split("-", 2)[:2]).upper()
        for name, text in [("PROJECTS.md", projects_md), ("VISUALS.md", visuals_md), ("EXECUTION.md", execution_md)]:
            if project_id not in text:
                fail(errors, f"{project_id} missing from {name}")

    for heading in range(1, 11):
        if f"## {heading}." not in projects_md:
            fail(errors, f"PROJECTS.md missing numbered group {heading}")


def run_command(errors: list[str], project: Path, command: list[str]) -> None:
    try:
        subprocess.run(command, cwd=project / "technical", check=True, capture_output=True, text=True, timeout=30)
    except subprocess.CalledProcessError as exc:
        fail(errors, f"{project.name}: entrypoint failed: {exc.stderr[-800:] or exc.stdout[-800:]}")
    except Exception as exc:
        fail(errors, f"{project.name}: entrypoint failed: {exc}")


def validate_entrypoints(errors: list[str], dirs: list[Path]) -> None:
    for project in dirs:
        ep = entrypoint(project)
        if ep.suffix == ".py":
            run_command(errors, project, [sys.executable, ep.name])
        elif ep.suffix == ".ts":
            run_command(errors, project, ["node", "--experimental-strip-types", ep.name])
        elif ep.suffix == ".R":
            run_command(errors, project, ["Rscript", ep.name])


def main() -> int:
    errors: list[str] = []
    dirs = validate_structure(errors)
    validate_visuals(errors, dirs)
    validate_json(errors)
    validate_python(errors)
    validate_links(errors)
    validate_secrets(errors)
    validate_manifests(errors, dirs)
    validate_indexes(errors, dirs)
    validate_entrypoints(errors, dirs)

    if errors:
        print("PORTFOLIO AUDIT FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Portfolio audit passed: {len(dirs)} projects")
    print(f"{len(dirs)}/{len(dirs)} principal execution files executed successfully.")
    print(f"{len(dirs)}/{len(dirs)} technical visuals passed structure and typography checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
