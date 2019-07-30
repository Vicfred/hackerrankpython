from collections import Counter

X = int(input())
sizes = list(map(int,input().split()))
shoes = Counter(sizes)
N = int(input())
earnings = 0
for idx in range(N):
    shoe_size, x = list(map(int,input().split()))
    if shoes[shoe_size] > 0:
        earnings += x
        shoes[shoe_size] -= 1
print(earnings)

