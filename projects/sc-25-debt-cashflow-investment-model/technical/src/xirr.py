from __future__ import annotations
from datetime import date

def xnpv(rate: float, cashflows: list[tuple[date, float]]) -> float:
    t0 = cashflows[0][0]
    return sum(value / ((1 + rate) ** ((dt - t0).days / 365.0)) for dt, value in cashflows)

def xirr(cashflows: list[tuple[date, float]], guess: float = 0.10) -> float:
    rate = guess
    for _ in range(100):
        f = xnpv(rate, cashflows)
        eps = 1e-6
        derivative = (xnpv(rate + eps, cashflows) - f) / eps
        if abs(derivative) < 1e-12:
            break
        next_rate = rate - f / derivative
        if abs(next_rate - rate) < 1e-9:
            return next_rate
        rate = next_rate
    return rate
