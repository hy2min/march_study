N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
lst =[]

def dfs(now):
    global lst
    lst.append(now)
    for i in range(N):
        if arr[now][i] == 1:
            dfs(i)

dfs(0)
print(*lst)