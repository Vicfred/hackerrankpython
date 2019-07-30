from itertools import combinations

ins = input().split()
s = ins[0]
k = int(ins[1])
s = list(s)
s.sort()
for idx in range(1,k+1):
    for x in combinations(s,idx):
        print(''.join(x))

