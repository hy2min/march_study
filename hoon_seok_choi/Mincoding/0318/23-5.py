friend = ['E', 'W', 'A', 'B', 'C']

n = input()
path = [0]*4
used = [0]*4

friend.remove(n)

def recur(depth):
    if depth == 4:
        for i in path:
            print(i,end='')
        print()
        return
    for i in range(4):
        if used[i] == 1:
            continue
        used[i] = 1
        path[depth] = friend[i]
        recur(depth+1)
        used[i] = 0

recur(0)
