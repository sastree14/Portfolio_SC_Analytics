def expected_cost(tp, fp, fn, review_cost=4.0, fraud_loss=250.0):
    return fp*review_cost + fn*fraud_loss
