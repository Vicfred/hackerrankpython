if __name__ == '__main__':
    N = int(input())
    current = list()
    for idx in range(N):
        ins = input().split()
        op = ins[0]
        if "insert" == op:
            i = int(ins[1])
            e = int(ins[2])
            current.insert(i,e)
        if "print" == op:
            print(current)
        if "remove" == op:
            e = int(ins[1])
            current.remove(e)
        if "append" == op:
            e = int(ins[1])
            current.append(e)
        if "sort" == op:
            current.sort()
        if "pop" == op:
            current.pop()
        if "reverse" == op:
            current.reverse()

