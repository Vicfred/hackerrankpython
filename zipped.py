N,X = list(map(int,input().split()))
subjects = []
for idx in range(X):
    subjects.append(list(map(float,input().split())))
for item in zip(*subjects):
    mean = sum(item)/X
    print('%.1f' % mean)
