name = input()

path = [0]*3
used = [0]*4

def recur(depth):
    if depth == 3:
        for i in path:
            print(i,end='')
        print()
        return
    for i in range(4):
        if used[i] == 1:
            continue
        used[i] = 1
        path[depth] = name[i]
        recur(depth+1)
        used[i] = 0

recur(0)