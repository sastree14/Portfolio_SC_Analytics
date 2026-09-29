"""SC-29 · Commercial Due Diligence & Market Intelligence System

MAIN EXECUTION FILE

This file is the clearest end-to-end public execution path for the project.
It keeps the major steps in one place so a reviewer can see how the project
runs without navigating the entire repository.
"""
from __future__ import annotations

import json
from pathlib import Path

TECHNICAL = Path(__file__).resolve().parent
PROJECT = TECHNICAL.parent
EXAMPLES = PROJECT / "examples"

QUESTIONS = {
    "market_growth": [
        {"source": "industry-report", "recency_days": 34, "confidence": 0.91},
        {"source": "company-filings", "recency_days": 18, "confidence": 0.87},
    ],
    "competition": [
        {"source": "competitor-sites", "recency_days": 7, "confidence": 0.79},
        {"source": "customer-reviews", "recency_days": 12, "confidence": 0.71},
        {"source": "industry-report", "recency_days": 34, "confidence": 0.84},
    ],
    "pricing_power": [
        {"source": "historical-pricing", "recency_days": 20, "confidence": 0.88},
    ],
}

def assess(question: str, evidence: list[dict]) -> dict:
    confidence = sum(x["confidence"] for x in evidence) / len(evidence)
    freshness = min(x["recency_days"] for x in evidence)
    status = "supported" if confidence >= 0.80 and len(evidence) >= 2 else "review"
    return {
        "question": question,
        "evidence_items": len(evidence),
        "mean_confidence": round(confidence, 3),
        "freshest_source_days": freshness,
        "status": status,
    }

def main() -> dict:
    assessments = [assess(question, evidence) for question, evidence in QUESTIONS.items()]
    result = {
        "assessments": assessments,
        "supported": sum(x["status"] == "supported" for x in assessments),
        "review_required": sum(x["status"] != "supported" for x in assessments),
    }
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()
