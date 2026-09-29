def amortization(principal,annual_rate,years):
    rate=annual_rate/12
    n=years*12
    payment=principal*rate/(1-(1+rate)**(-n))
    balance=principal; rows=[]
    for m in range(1,n+1):
        interest=balance*rate; principal_paid=payment-interest; balance=max(0,balance-principal_paid)
        rows.append((m,payment,interest,principal_paid,balance))
    return rows
