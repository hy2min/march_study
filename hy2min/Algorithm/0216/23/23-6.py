lst = list(map(int, input()))
path = [0] * 4
cnt = 0

def abc(level):
    global cnt
    if level == 4:
        for i in range(3):
            if abs(path[i+1]-path[i]) > 3:
                return
        cnt += 1
        return
    
    for i in range(5):
        path[level] = lst[i]
        abc(level+1)

abc(0)
print(cnt)