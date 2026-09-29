def expected_contribution(amount, rate, pd, lgd, funding_cost):
    revenue=amount*rate
    expected_loss=amount*pd*lgd
    cost=amount*funding_cost
    return revenue-expected_loss-cost
