import sys
from collections import deque
sys.stdin = open("sample_input.txt","r")

def dfs(y,x,cnt):
    if cnt == l:
        return

    if arr[y][x] != 0:
        for i in pipe[arr[y][x]]:
            dy = y + i[0]
            dx = x + i[1]
            if dy < 0 or dx < 0 or dy >= n or dx >= m:
                continue
            visited[dy][dx] = 1
            dfs(dy, dx, cnt+1)

def bfs(y, x, cnt):
    q = deque([(r,c)])
    # visited = [[0]*m for _ in range(n)]
    # visited[r][c] = 1

    while q:
        y, x = q.popleft()
        if cnt == l:
            continue

        for d_y,d_x in pipe[arr[y][x]]:
            dy = y+d_y
            dx = x+d_x

            if dy < 0 or dx < 0 or dy >= n or dx >= m:
                continue
            if visited[dy][dx] == 0 and arr[dy][dx] != 0:
                visited[dy][dx] = 1
                cnt+=1
                q.append([dy,dx])

    return

pipe = {
    1:[(-1,0),(1,0),(0,-1),(0,1)],
    2:[(-1,0),(1,0)],
    3:[(0,-1),(0,1)],
    4:[(-1,0),(0,1)],
    5:[(1,0),(0,1)],
    6:[(0,-1),(1,0)],
    7:[(0,-1),(-1,0)]
}


t = int(input())
for tc in range(1, t+1):
    n,m,r,c,l = map(int, input().split())
    visited = [[0]*m for _ in range(n)]
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited[r][c] = 1
    bfs(r,c,1)
    ans = 0
    for i in visited:
        ans += i.count(1)
    print(f'#{tc} {ans}')