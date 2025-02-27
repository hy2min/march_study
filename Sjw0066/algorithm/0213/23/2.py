def abc(level):
    global cnt

    if level==4:
        cnt+=1
        return

    for i in range(4):
        if level>0 :
            if path[level-1] == 'T' and name[i]=='B':
                continue
            if path[level-1] == 'B' and name[i]=='T':
                continue

        path[level] = name[i]
        abc(level+1)
        path[level] = 0

cnt=0
path=[0]*4
name=list(input())



abc(0)
print(cnt)

