from itertools import permutations

ins = input().split()
s = ins[0]
k = int(ins[1])
s = list(s)
s.sort()
for x in permutations(s,k):
    print(''.join(x))

