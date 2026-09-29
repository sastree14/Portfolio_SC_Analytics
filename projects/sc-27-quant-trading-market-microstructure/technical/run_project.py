"""SC-27 · Quantitative Trading & Market Microstructure System

MAIN EXECUTION FILE

This file is the clearest end-to-end public execution path for the project.
It keeps the major steps in one place so a reviewer can see how the project
runs without navigating the entire repository.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT.parent / "examples"

EVENTS = [
    {"bid": 99.9, "ask": 100.1, "bid_size": 420, "ask_size": 310, "trade": 100.1, "size": 85},
    {"bid": 100.0, "ask": 100.2, "bid_size": 510, "ask_size": 260, "trade": 100.2, "size": 110},
    {"bid": 100.1, "ask": 100.3, "bid_size": 390, "ask_size": 470, "trade": 100.1, "size": 65},
    {"bid": 100.2, "ask": 100.4, "bid_size": 620, "ask_size": 280, "trade": 100.4, "size": 140},
]

def features(event: dict) -> dict:
    total = event["bid_size"] + event["ask_size"]
    imbalance = (event["bid_size"] - event["ask_size"]) / total
    mid = (event["bid"] + event["ask"]) / 2
    signed_delta = event["size"] if event["trade"] >= mid else -event["size"]
    return {"mid": round(mid, 4), "imbalance": round(imbalance, 4), "signed_delta": signed_delta}

def signal(feature: dict) -> int:
    if feature["imbalance"] > 0.20 and feature["signed_delta"] > 0:
        return 1
    if feature["imbalance"] < -0.20 and feature["signed_delta"] < 0:
        return -1
    return 0

def main() -> dict:
    rows = []
    position = 0
    pnl = 0.0
    last_mid = None
    for event in EVENTS:
        feat = features(event)
        if last_mid is not None:
            pnl += position * (feat["mid"] - last_mid)
        position = signal(feat)
        last_mid = feat["mid"]
        rows.append({"event": event, "features": feat, "signal": position, "cumulative_pnl": round(pnl, 4)})
    result = {"events": rows, "ending_pnl": round(pnl, 4)}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()
