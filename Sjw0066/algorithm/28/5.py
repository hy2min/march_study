def dfs(now,level):

    if level==2:
        for i in range(len(path)):
            print(path[i],end=" ")
        print()
        return


    for i in range(N):
        if arr[now][i] :
            path[level+1]=name[i]
            dfs(i,level+1)
            path[level+1]=0



N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
name=[i for i in range(N)]
path=[0]*3
dfs(0,0)
