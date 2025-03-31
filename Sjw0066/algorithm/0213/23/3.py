def abc(level):
    global cnt

    if level==n:
        cnt+=1
        return

    for i in range(3):
        if level>1 :
            if path[level-1] == name[i] and path[level-2] == name[i]:
                continue
        path[level] = name[i]
        abc(level+1)
        path[level] = 0

cnt=0
n=int(input())
path=[0]*n
name=['A','B','C']
abc(0)
print(cnt)

