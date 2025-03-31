import sys
from collections import deque
sys.stdin = open("sample_input.txt","r")


def bfs(r, c, cnt):
    q = deque()
    q.append((r, c, cnt))

    while q:
        y, x, cnt = q.popleft()

        if cnt == l:
            return

        for d_y, d_x in pipe[arr[y][x]]:
            dy = y + d_y
            dx = x + d_x

            if dy < 0 or dx < 0 or dy >= n or dx >= m:
                continue
            if arr[dy][dx] == 0 or visited[dy][dx] == 1:
                continue
            if (-d_y, -d_x) not in pipe[arr[dy][dx]]:
                continue
            visited[dy][dx] = 1
            q.append((dy, dx, cnt+1))





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
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    bfs(r, c, 1)

    ans = 0
    for i in visited:
        ans += i.count(1)
    print(f'#{tc} {ans}')