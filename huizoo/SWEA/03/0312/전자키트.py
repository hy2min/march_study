t = int(input())
for tc in range(1, t+1):
    if tc == 3:
        debug = 1
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    Min = 21e8
    visited = [0]*n
    def abc(level, x, Sum):
        global Min
        if level == n:
            Min = min(Min, Sum)
            return
        if Min < Sum:
            return
        if level == n-1:
            visited[0] = 0
        for i in range(n):
            if arr[x][i] and not visited[i]:
                visited[i] = 1
                abc(level + 1, i, Sum+arr[x][i])
                visited[i] = 0
        if level == n-1:
            visited[0] = 1
    visited[0] = 1
    abc(0, 0, 0)
    print(f'#{tc} {Min}')