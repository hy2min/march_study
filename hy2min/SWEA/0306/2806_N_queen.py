def dfs(level):
    global cnt
    if level == n:
        cnt += 1
        return

    for i in range(n):
        if visited[i] == 0 and r_visited[level+i] == 0 and l_visited[level-i+n-1] == 0:
            visited[i] = r_visited[level+i] = l_visited[level-i+n-1] = 1
            dfs(level+1)
            visited[i] = r_visited[level+i] = l_visited[level-i+n-1] = 0


t = int(input())
for tc in range(1, t+1):
    
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    cnt = 0
    visited = [0] * n
    r_visited = [0] * (2*n-1)
    l_visited = [0] * (2*n-1)

    dfs(0)
    print(f'#{tc} {cnt}')
