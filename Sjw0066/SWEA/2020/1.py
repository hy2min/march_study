n=int(input())

def abc(level):
    global cnt
    if level==3:
        cnt+=1
        return

    for i in range(n):
        if used[i] == 1 : continue
        used[i] = 1
        abc(level+1)
        used[i] = 0


used=[0]*n
cnt=0
abc(0)
print(cnt)