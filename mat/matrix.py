import numpy as np
 
class Matrix:
    def __init__(self, alpha, eps):
        self.alpha = alpha
        self.eps = eps

    def iteration(self, x_0, A, b):
        E = np.identity(A.shape[0])
        y = (E-self.alpha*A) @ x_0
        x_k = y  + self.alpha*b
        C = max(abs(x_k_i - x_0_i) for x_k_i, x_0_i in zip(x_k, x_0))
        while (C > self.eps):
            y = (E-self.alpha*A) @ x_k
            x_0 = x_k.copy()
            x_k = y + self.alpha*b
            C = max(abs(x_k_i - x_0_i) for x_k_i, x_0_i in zip(x_k, x_0))
        return x_k
