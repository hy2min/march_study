s = input()
path = [""] * 4
cnt = 0

def abc(level):
    global cnt

    if level == 4:
        for i in range(3):
            if (path[i] == 'B' and path[i+1] == 'T') or (path[i] == 'T' and path[i+1] == 'B'):
                return
        cnt += 1
        return

    for i in range(4):
        path[level] = s[i]
        abc(level + 1)

abc(0)
print(cnt)