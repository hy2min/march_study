import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline().strip())
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
visited = [[False]*N for _ in range(N)]
cnt1 = 0
cnt2 = 0

def dfs(y, x, color, is_rg_blind):
    for dy, dx in d:
        ny, nx = y+dy, x+dx
        if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
        if visited[ny][nx]: continue
        if is_rg_blind:
            if (color in "RG" and arr[ny][nx] in "RG") or (color == "B" and arr[ny][nx] == "B"):
                visited[ny][nx] = True
                dfs(ny, nx, color, is_rg_blind)
        else:
            if arr[ny][nx] == color:
                visited[ny][nx] = True
                dfs(ny, nx, color, is_rg_blind)


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt1 += 1
            visited[i][j] = True
            dfs(i, j, arr[i][j], False)

visited = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt2 += 1
            visited[i][j] = True
            dfs(i, j, arr[i][j], True)

print(cnt1, cnt2)