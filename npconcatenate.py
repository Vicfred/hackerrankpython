import numpy as np

N, M, P = list(map(int, input().split()))
A = []
B = []
for idx in range(N):
    A.append(list(map(int, input().split())))
for idx in range(M):
    B.append(list(map(int, input().split())))
print(np.concatenate((A, B), axis=0))

