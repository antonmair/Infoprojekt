import numpy as np
def make_r(k, anglist):    
    r = np.zeros(2**k, dtype=float)
    if k == 0:
        r[0] = 3 * anglist[0] + 3 * anglist[1]
        return r
    r[0] = 4 * anglist[0] + 2 * anglist[1]
    for i in range(1, 2**(k)):
        r[i] = 2 * anglist[i] + 2 * anglist[i + 1]
    r[-1] = 2 * anglist[-2] + 4 * anglist[-1]
    return r