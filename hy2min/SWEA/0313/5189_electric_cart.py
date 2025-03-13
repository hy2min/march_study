def dfs(level, now, total):
    global mn
    if level == n-1:
        total += arr[now][0]
        if mn > total:
            mn = total
        return

    for i in range(1, n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(level+1, i, total + arr[now][i])
            visited[i] = 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    visited[0] = 1
    mn = 21e8
    total = 0

    dfs(0, 0, 0)


    print(f'#{tc} {mn}')
