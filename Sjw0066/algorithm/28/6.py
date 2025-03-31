name=list(input())

arr=[list(map(int,input().split())) for _ in range(8)]

def dfs(now):

    print(name[now],end="")

    for i in range(8):
        if arr[now][i]:
            dfs(i)

dfs(0)