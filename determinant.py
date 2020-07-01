#Finding the determinant

import numpy as np

n = int(input())
matrix = []
for i in range(0, n):
    a = list(map(float,input().split()))
    matrix.append(a)

print(round(np.linalg.det(matrix), 2))
