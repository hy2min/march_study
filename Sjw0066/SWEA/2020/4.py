n=int(input())
lst=list(map(int,input().split()))
Min=21e8
used=[0]*n
def abc(Sum,level):
    global Min

    if level==3:
        Min=min(Sum,Min)
        return

    for i in range(n):
        if used[i] == 1: continue
        if lst[i] == 0 and level==0: continue
        used[i] = 1
        abc(Sum*10+lst[i],level+1)
        used[i] = 0

abc(0,0)
print(Min)

