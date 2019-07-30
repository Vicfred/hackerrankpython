import numpy

row = input()
row = row.split()
row = list(map(int,row))
A = numpy.array(row)
row = input()
row = row.split()
row = list(map(int,row))
B = numpy.array(row)
print(numpy.inner(A,B))
print(numpy.outer(A,B))
