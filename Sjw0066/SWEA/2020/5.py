n,m=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]
Max=-21e8
used=[[0]*4 for _ in range(n)]
path=[0]*3
Max_path=[]
def abc(Sum,level):
    global Max,Max_path

    if level==n:
        if Sum>Max:
            Max=max(Sum,Max)
            Max_path=path[:]
        return

    for i in range(n):
        for j in range(m):
            if used[i][j] == 1 :continue
            used[i][j] = 1
            path[level] = lst[i][j]
            abc(Sum+lst[i][j],level+1)
            path[level] = 0
            used[i][j] = 0



abc(0,0)
Max_path.sort(reverse=True)
for k in range(n):
    for i in range(n):
        flag=0
        for j in range(m):
            if Max_path[k] == lst[i][j] :
                print(f'{lst[i][j]}({i},{j})')
                flag=1
                break
        if flag:
            break