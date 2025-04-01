string = input()
path = [0]*4
cnt = 0
def abc(lev):
    global cnt, path
    if lev == 4:
        cnt += 1
        print(path)
        return

    for i in range(4):
        path[lev] = string[i]
        if i > 0:
            if path[lev-1] == 'B' and path[lev] == 'T':
                continue
            elif path[lev-1] == 'T' and path[lev] == 'B':
                continue
        abc(lev+1)


abc(0)
print(cnt)
