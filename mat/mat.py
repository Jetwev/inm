from matrix import *

mat = Matrix(alpha=0.1, eps=0.001)
A = np.array([[10, -1, 0 ,1], [0 ,12 ,1, -1], [1 ,-2 ,16 ,0], [0 ,2 ,0 ,16]])
b = np.array([0, -28 , 31, 29]) 
x0 = np.array([1, 0, 0, 0])

print(mat.iteration(x0, A, b))
