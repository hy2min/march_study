n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

def dfs(now):

    print(now,end=" ")

    for i in range(n):
        if arr[now][i]:
            dfs(i)

dfs(0)