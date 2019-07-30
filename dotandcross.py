import numpy

N = int(input())
matrix = []
for idx in range(N):
    row = input()
    row = row.split()
    row = list(map(int,row))
    matrix.append(row)
A = numpy.array(matrix)
matrix = []
for idx in range(N):
    row = input()
    row = row.split()
    row = list(map(int,row))
    matrix.append(row)
B = numpy.array(matrix)
print(numpy.matmul(A,B))
