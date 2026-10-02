from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
projects = root / "projects"
catalog = root / "catalog"

required_project_files = [
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
]

required_manifest_markers = [
    "schema_version: 2",
    "project_type: public-portfolio-implementation",
    "designed_for:",
    "why_it_matters:",
    "technologies:",
    "provenance:",
    "evidence_class: public_portfolio_implementation",
    "client_claim_allowed: false",
    "evidence:",
    "business_impact:",
    "results:",
    "architecture:",
    "technical_decisions:",
    "limitations:",
    "visuals:",
    "execution:",
    "paths:",
]

errors = []
dirs = sorted(p for p in projects.iterdir() if p.is_dir() and p.name.startswith("sc-"))

if len(dirs) != 32:
    errors.append(f"expected 32 project directories, found {len(dirs)}")

for project in dirs:
    for rel in required_project_files:
        if not (project / rel).exists():
            errors.append(f"{project.name}: missing {rel}")

    manifest = catalog / f"{project.name}.yml"
    if not manifest.exists():
        errors.append(f"{project.name}: missing catalog manifest")
        continue

    text = manifest.read_text(encoding="utf-8")
    for marker in required_manifest_markers:
        if marker not in text:
            errors.append(f"{project.name}: manifest missing {marker}")

    project_id = "-".join(project.name.split("-", 2)[:2]).upper()
    if not re.search(rf"^id:\s*{re.escape(project_id)}\s*$", text, re.MULTILINE):
        errors.append(f"{project.name}: manifest id does not match {project_id}")

    referenced = re.findall(r"^\s{2}[a-z_]+:\s+(projects/[^\n]+)$", text, re.MULTILINE)
    for rel in referenced:
        if not (root / rel.strip()).exists():
            errors.append(f"{project.name}: manifest path does not exist: {rel.strip()}")

index = (catalog / "projects.yml").read_text(encoding="utf-8")
for project in dirs:
    manifest_path = f"catalog/{project.name}.yml"
    if manifest_path not in index:
        errors.append(f"{project.name}: manifest missing from catalog/projects.yml")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print(f"Portfolio structure and manifests valid: {len(dirs)} projects")
