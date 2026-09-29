# Portfolio quality

The portfolio is checked as a product, not only as a folder of code.

The automated audit verifies:

- exactly 29 project directories
- required business and technical documentation
- analytical visual evidence for every project except the two native-BI screenshot exceptions
- JSON validity
- Python syntax
- local Markdown links
- obvious committed-secret patterns
- project catalogue coverage
- deterministic local example execution where the entry point has no third-party runtime dependency

## Native BI exception

SC-14 (Power BI) and SC-15 (Tableau) are structurally complete, but native screenshots are intentionally excluded until genuine native-tool visual references are available. The audit treats this as an explicit temporary exception rather than silently accepting missing evidence.
