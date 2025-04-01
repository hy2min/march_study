friend = ['E', 'W', 'A', 'B', 'C']
path = [0]*4
used = [0]*4
out = input()
friend.pop(friend.index(out))

def abc(lev):
    global path
    if lev == 4:
        print(*path, sep = '')
        return

    for i in range(4):
        if used[i] == 0:
            used[i] = 1
            path[lev] = friend[i]
            abc(lev+1)
            used[i] = 0
        continue

abc(0)

