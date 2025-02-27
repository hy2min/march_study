def abc(level):

    if level==3:
        for i in range(3):
            print(path[i],end="")
        print()
        return

    for i in range(4):
        if used[i] ==1:
            continue
        used[i] = 1
        path[level] = name[i]
        abc(level+1)
        path[level] = 0
        used[i] = 0

path=[0]*3
used=[0]*4
name=list(input())
abc(0)
