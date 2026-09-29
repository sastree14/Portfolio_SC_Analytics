from pathlib import Path
import sys

root=Path(__file__).resolve().parents[1]
projects=root/"projects"
required=[
    "README.md",
    "docs/BUSINESS_IMPACT.md",
    "docs/ARCHITECTURE.md",
    "docs/CREDENTIALS_AND_INTEGRATIONS.md",
    "docs/ENVIRONMENTS.md",
    "docs/LIMITATIONS.md",
    "technical/README.md",
]
errors=[]
dirs=sorted(p for p in projects.iterdir() if p.is_dir() and p.name.startswith("sc-"))
for p in dirs:
    for rel in required:
        if not (p/rel).exists():
            errors.append(f"{p.name}: missing {rel}")
if len(dirs)!=29:
    errors.append(f"expected 29 project directories, found {len(dirs)}")
if errors:
    print("\n".join(errors)); sys.exit(1)
print(f"Portfolio structure valid: {len(dirs)} projects")
