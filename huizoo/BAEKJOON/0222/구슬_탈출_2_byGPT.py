import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

red, blue, hole = None, None, None
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            red = (i, j)
        elif arr[i][j] == 'B':
            blue = (i, j)
        elif arr[i][j] == 'O':
            hole = (i, j)


def move(y, x, dy, dx):
    count = 0  # 해당 방향으로 이동한 횟수
    # 다음 칸이 벽('#')가 아니고 현재 칸이 구멍이 아닐 때까지 이동
    while arr[y + dy][x + dx] != '#' and arr[y][x] != 'O':
        y += dy
        x += dx
        count += 1
        if (y, x) == hole:  # 구멍에 도달하면 바로 종료
            break
    return y, x, count


def bfs():
    q = deque()
    q.append((red, blue, 0))
    visited = set()
    visited.add((red, blue))

    # 10번 이하의 이동으로 해결 가능해야 함.
    while q:
        r_pos, b_pos, cnt = q.popleft()
        if cnt >= 10:
            break
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # 빨간 구슬 이동
            r_ny, r_nx, r_moves = move(r_pos[0], r_pos[1], dy, dx)
            # 파란 구슬 이동
            b_ny, b_nx, b_moves = move(b_pos[0], b_pos[1], dy, dx)

            # 파란 구슬이 구멍에 들어가면 이 방향은 실패
            if (b_ny, b_nx) == hole:
                continue
            # 빨간 구슬만 구멍에 들어갔으면 성공!
            if (r_ny, r_nx) == hole:
                return cnt + 1

            # 두 구슬이 같은 위치에 있다면, 더 많이 이동한 구슬을 한 칸 뒤로 보정
            if (r_ny, r_nx) == (b_ny, b_nx):
                if r_moves > b_moves:
                    r_ny -= dy
                    r_nx -= dx
                else:
                    b_ny -= dy
                    b_nx -= dx

            if ((r_ny, r_nx), (b_ny, b_nx)) not in visited:
                visited.add(((r_ny, r_nx), (b_ny, b_nx)))
                q.append(((r_ny, r_nx), (b_ny, b_nx), cnt + 1))
    return -1


print(bfs())
