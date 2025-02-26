card = list(map(int, input()))
path = [0]*4
cnt = 0

def abc(lev):
    global path, cnt
    if lev == 4:
        for i in range(3):
            if abs(path[i] - path[i+1]) > 3:
                return
        cnt += 1
        return

    for i in range(5):
        path[lev] = card[i]
        abc(lev + 1)


abc(0)
print(cnt)