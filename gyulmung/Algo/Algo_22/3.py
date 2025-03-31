lev = int(input())
path = [0]*4
name = 'BGTK'

def abc(level):
    global path
    if level == lev:
        for i in range(level):
            print(path[i], end = '')
        print()
        return

    for i in range(4):
        path[level] = name[i]
        abc(level + 1)
        path[level] = 0



abc(0)