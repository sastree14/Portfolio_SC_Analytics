"""SC-25 · Debt, Cash Flow & Investment Model

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

from datetime import date

def amortization(principal: float, annual_rate: float, years: int) -> list[dict]:
    monthly = annual_rate / 12
    periods = years * 12
    payment = principal * monthly / (1 - (1 + monthly) ** (-periods))
    balance = principal
    rows = []
    for month in range(1, periods + 1):
        interest = balance * monthly
        principal_paid = payment - interest
        balance = max(0.0, balance - principal_paid)
        rows.append({
            "month": month,
            "payment": round(payment, 2),
            "interest": round(interest, 2),
            "principal": round(principal_paid, 2),
            "balance": round(balance, 2),
        })
    return rows

def xnpv(rate: float, cashflows: list[tuple[date, float]]) -> float:
    start = cashflows[0][0]
    return sum(value / ((1 + rate) ** ((dt - start).days / 365)) for dt, value in cashflows)

def main() -> dict:
    schedule = amortization(1_200_000, 0.055, 10)
    cashflows = [
        (date(2026, 1, 1), -600000),
        (date(2027, 6, 1), 120000),
        (date(2028, 6, 1), 160000),
        (date(2029, 6, 1), 210000),
        (date(2030, 6, 1), 460000),
    ]
    result = {
        "first_12_months": schedule[:12],
        "year_1_debt_service": round(sum(x["payment"] for x in schedule[:12]), 2),
        "npv_at_10pct": round(xnpv(0.10, cashflows), 2),
    }
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()
