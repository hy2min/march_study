friends = input() #네명의 친구들의 이름 입력받기
path = [0]*3
used = [0]*4


def abc(lev):
    global path, used
    if lev == 3:
        print(*path,sep='')
        return

    for i in range(4):
        if used[i] == 1: continue
        path[lev] = friends[i]
        used[i] = 1
        abc(lev+1)
        path[lev] = 0
        used[i] = 0
abc(0)