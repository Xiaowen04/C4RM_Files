import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    t = np.arange(1, n + 1)
   
    discount = (1 + y / ppy )** (-t)
    price = np.sum(face * couponRate / ppy * discount) + face * discount[-1]
    return price