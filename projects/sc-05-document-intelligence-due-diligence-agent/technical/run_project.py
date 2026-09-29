"""SC-05 · Document Intelligence & Due Diligence Agent

MAIN EXECUTION FILE

This file is the clearest end-to-end public execution path for the project.
It intentionally keeps the major steps in one place so a reviewer can see
how input becomes a business output without navigating the whole codebase.
Supporting modules under src/, sql/, workflows/ and infra/ provide the deeper
implementation details.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT.parent / "examples"

import re

def chunk(text: str, size: int = 220) -> list[str]:
    words = text.split()
    return [" ".join(words[i:i + size]) for i in range(0, len(words), size)]

def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z]{3,}", text.lower()))

def retrieve(question: str, chunks: list[str], k: int = 3) -> list[dict]:
    q = tokenize(question)
    scored = []
    for i, text in enumerate(chunks):
        overlap = len(q & tokenize(text))
        scored.append({"chunk_id": i, "score": overlap, "text": text})
    return sorted(scored, key=lambda x: x["score"], reverse=True)[:k]

def synthesize(question: str, evidence: list[dict]) -> dict:
    return {
        "question": question,
        "answer": "Finding generated only from the retrieved public evidence.",
        "evidence": [{"chunk_id": x["chunk_id"], "score": x["score"]} for x in evidence],
        "requires_human_review": True,
    }

def main() -> dict:
    document = (
        "The supplier agreement renews annually. Termination requires ninety days notice. "
        "Pricing can be revised once per year subject to a five percent cap. "
        "The customer concentration section notes that the largest customer represents twenty eight percent of revenue."
    )
    chunks = chunk(document)
    question = "What are the renewal and termination conditions?"
    evidence = retrieve(question, chunks)
    result = synthesize(question, evidence)
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()
