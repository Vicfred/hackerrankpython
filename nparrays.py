import numpy

def arrays(arr):
    return numpy.array(list(reversed(arr)), float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
