import numpy as np
def make_matrix(k):
    n = 2 ** k
    A = np.zeros((n, n), dtype=float)
    A[np.arange(n), np.arange(n)] = 6
    A[0, 0] = 7
    A[-1, -1] = 7
    idx = np.arange(n - 1)
    A[idx, idx + 1] = 1
    A[idx + 1, idx] = 1
    if n == 1: #hotfix 19.03.26 to include mathematical optimum which would be 6 not 7
        A[0,0] = 6
    return A