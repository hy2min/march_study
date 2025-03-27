# 용사여, 이세계를 구하여라!
import sys
from collections import deque
input = sys.stdin.readline

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def fight(start, end):
    sty, stx = start
    eny, enx = end
    q = deque([start])
    visited = [[-1]*M for _ in range(N)]
    visited[sty][stx] = 0
    while q:
        yy, xx = q.popleft()
        for dy, dx in d:
            ny, nx = yy+dy, xx+dx
            if ny<0 or nx<0 or ny>=N or nx>=M: continue
            if ny==eny and nx==enx: return visited[yy][xx] + 1
            if visited[ny][nx] == -1 and arr[ny][nx] != 'x':
                visited[ny][nx] = visited[yy][xx] + 1
                q.append((ny, nx))

    return 0

def adventure():
    # 바위가 막고 있으면 이동 불가
    # 마왕은 체력을 가지고 있고 움직이지 않음
    # 공격력은 '1'의 시간동안 마왕에게 입힐 수 있는 데미지를 의미
    # 무기를 획득해서 가야함, 1개만 획득 가능
    # Y 칼리버는 공격력 5, 나무막대기는 공격력 2
    Min = 1e9
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'S':
                s = (i, j)
            elif arr[i][j] == 'Y':
                y = (i, j)
            elif arr[i][j] == 'T':
                t = (i, j)
            elif arr[i][j] == 'M':
                m = (i, j)

    y_cnt = fight(y, s)
    y_cnt2 = fight(s, m)
    if y_cnt == 0 or y_cnt2 == 0:
        pass
    else:
        y_cnt3 = hp//5 if hp%5 == 0 else hp//5 + 1
        Min = min(Min, y_cnt + y_cnt2 + y_cnt3)

    t_cnt = fight(y, t)
    t_cnt2 = fight(t, m)
    if t_cnt == 0 or t_cnt2 == 0:
        pass
    else:
        t_cnt3 = hp//2 if hp%2 == 0 else hp//2 + 1
        Min = min(Min, t_cnt + t_cnt2 + t_cnt3)

    if Min == 1e9:
        print(f'#{tc} the world is doomed')
    else:
        print(f'#{tc} {Min}')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    hp = int(input())
    adventure()
