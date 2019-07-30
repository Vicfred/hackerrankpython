from collections import deque
d = deque()
N = int(input())
for idx in range(N):
    ins = input()
    ins = ins.split()
    operation = ins[0]
    x = 0
    if len(ins) == 2:
        x = int(ins[1])
    if "append" == operation:
        d.append(x)
    if "pop" == operation:
        d.pop()
    if "appendleft" == operation:
        d.appendleft(x)
    if "popleft" == operation:
        d.popleft()
for x in d:
    print(x, end=' ')
print()
