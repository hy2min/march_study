def dfs(now):

    print(name[now],end=" ")

    for i in range(N):
        if arr[now][i] :
            dfs(i)



N=int(input())

arr=[list(map(int,input().split())) for _ in range(N)]
name=[0,1,2,3,4,5,6]
dfs(0)
