import numpy as np
from matrixmaket import make_matrix 
from rmaker import make_r
def anglepunishment(k, anglist):
      A = make_matrix(k)
      r = make_r(k, anglist)
      newanglist = np.linalg.solve(A, r)
      return newanglist