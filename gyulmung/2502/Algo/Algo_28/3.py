family = [[0, 1, 1, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 1, 0, 1, 0],
          [0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]]
name=['A','B','C','D','E','F','G','H']

who = input()
level = -1
bro = []

def where(now):
    global level
    for i in range(8):
        if family[now][i] == 1 and who == name[i]:
            level = now
            return
        elif family[now][i] == 1:
            where(i)

where(0)
if level == -1:
    print('없음')
else:
    for i in range(8):
        if family[level][i] == 1:
            bro.append(name[i])
    bro.pop(bro.index(who))
    print(*bro)