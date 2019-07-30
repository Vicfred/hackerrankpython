if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort()
    best = arr[len(arr)-1]
    for i in reversed(range(0,len(arr))):
        if arr[i] < best:
            print(arr[i])
            break

