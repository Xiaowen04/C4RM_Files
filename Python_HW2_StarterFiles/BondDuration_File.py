import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    n = m * ppy
    t = np.arange(1, n + 1)
   
    discount = (1 + y / ppy)** (-t)

    coupon = face * couponRate / ppy
    cashflows = np.full(n, coupon)
    cashflows[-1] = cashflows[-1] + face

    pv = cashflows * discount

    duration = np.sum((t / ppy) * pv) / np.sum(pv)

    return duration