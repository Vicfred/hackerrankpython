import numpy as np

N, M = list(map(int, input().split()))
A = []
for idx in range(N):
    A.append(list(map(int, input().split())))
print(np.prod(np.sum(A, axis=0)))
