name=['B','T','S','K','R']
n=int(input())
path=[0]*n
used=[0]*5
cnt=0
def abc(level):
    global cnt

    if level == n :
        if used[2] == 1:
            cnt+=1
        return

    for i in range(5):
        if used[i] == 1:
            continue
        used[i] = 1
        path[level] = name[i]
        abc(level+1)
        path[level]=0
        used[i] = 0

abc(0)
print(cnt)