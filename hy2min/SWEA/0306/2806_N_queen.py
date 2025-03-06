

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    dfs(0,0)
    print(cnt)