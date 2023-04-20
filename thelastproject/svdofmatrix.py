import numpy as np
from scipy.linalg import svd
"""Singular Value Decomposition"""
# define a matrix
X = np.array([[1,0,1,0], [0,1,0,1]])
print(X)
# perform SVD
U, singular, V_transpose = svd(X)
# print different components
print("U: ",U)
print("Singular array",singular)
print("V^{T}",V_transpose)