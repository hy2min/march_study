import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
L = max(N, M)-2
# . 빈칸 # 벽 o 구멍 R 빨강 B 파랑
bead = dict()
for i in range(1, N-1):
    for j in range(1, M-1):
        if arr[i][j] == 'R':
            bead['R'] = (i, j)
        if arr[i][j] == 'B':
            bead['B'] = (i, j)
        if arr[i][j] == 'O':
            hole = (i, j)
bead['cnt'] = 0
def abc():
    q = deque()
    q.append(bead)
    ans = 0
    while q:
        now = q.popleft()
        ry, rx = now['R']
        by, bx = now['B']
        cnt = now['cnt']
        if cnt == 10:
            return -1
        for i in range(4):
            pos = 1
            nry, nrx = ry, rx
            nby, nbx = by, bx
            if i == 0:
                if ry < by:
                    while 1:
                        if nry-1 < 1 or nry-1 >= N-1: break
                        if arr[nry-1][nrx] == '#': break
                        if arr[nry-1][nrx] == 'O':
                            ans = cnt+1
                            nry = 0
                            break
                        nry -= 1
                    while 1:
                        if nby-1 < 1 or nby-1 >= N-1: break
                        if arr[nby-1][nbx] == '#': break
                        if nby-1 == nry and nbx == nrx: break
                        if arr[nby-1][nbx] == 'O':
                            pos = 0
                            break
                        nby -= 1
                else:
                    while 1:
                        if nby-1 < 1 or nby-1 >= N-1: break
                        if arr[nby-1][nbx] == '#': break
                        if arr[nby-1][nbx] == 'O':
                            pos = 0
                            break
                        nby -= 1
                    while 1:
                        if nry-1 < 1 or nry-1 >= N-1: break
                        if arr[nry-1][nrx] == '#': break
                        if nry-1 == nby and nbx == nrx: break
                        if arr[nry-1][nrx] == 'O':
                            ans = cnt+1
                            nry = 0
                            break
                        nry -= 1
            elif i == 1:
                if rx < bx:
                    while 1:
                        if nrx-1 < 1 or nrx-1 >= M-1: break
                        if arr[nry][nrx-1] == '#': break
                        if arr[nry][nrx-1] == 'O':
                            ans = cnt+1
                            nrx = 0
                            break
                        nrx -= 1

                    while 1:
                        if nbx-1 < 1 or nbx-1 >= M-1: break
                        if arr[nby][nbx-1] == '#': break
                        if nbx-1 == nrx and nby == nry: break
                        if arr[nby][nbx-1] == 'O':
                            pos = 0
                            break
                        nbx -= 1
                else:
                    while 1:
                        if nbx-1 < 1 or nbx-1 >= M-1: break
                        if arr[nby][nbx-1] == '#': break
                        if arr[nby][nbx-1] == 'O':
                            pos = 0
                            break
                        nbx -= 1
                    while 1:
                        if nrx-1 < 1 or nrx-1 >= M-1: break
                        if arr[nry][nrx-1] == '#': break
                        if nrx-1 == nbx and nby == nry: break
                        if arr[nry][nrx-1] == 'O':
                            ans = cnt+1
                            nrx = 0
                            break
                        nrx -= 1
            elif i == 2:
                if rx > bx:
                    while 1:
                        if nrx+1 < 1 or nrx+1 >= M-1: break
                        if arr[nry][nrx+1] == '#': break
                        if arr[nry][nrx+1] == 'O':
                            ans = cnt+1
                            nrx = 0
                            break
                        nrx += 1
                    while 1:
                        if nbx+1 < 1 or nbx+1 >= M-1: break
                        if arr[nby][nbx+1] == '#': break
                        if nbx+1 == nrx and nby == nry: break
                        if arr[nby][nbx+1] == 'O':
                            pos = 0
                            break
                        nbx += 1
                else:
                    while 1:
                        if nbx+1 < 1 or nbx+1 >= M-1: break
                        if arr[nby][nbx+1] == '#': break
                        if arr[nby][nbx+1] == 'O':
                            pos = 0
                            break
                        nbx += 1
                    while 1:
                        if nrx+1 < 1 or nrx+1 >= M-1: break
                        if arr[nry][nrx+1] == '#': break
                        if nrx+1 == nbx and nby == nry: break
                        if arr[nry][nrx+1] == 'O':
                            ans = cnt+1
                            nrx = 0
                            break
                        nrx += 1
            elif i == 3:
                if ry > by:
                    while 1:
                        if nry+1 < 1 or nry+1 >= N-1: break
                        if arr[nry+1][nrx] == '#': break
                        if arr[nry+1][nrx] == 'O':
                            ans = cnt+1
                            nry = 0
                            break
                        nry += 1
                    while 1:
                        if nby+1 < 1 or nby+1 >= N-1: break
                        if arr[nby+1][nbx] == '#': break
                        if nby+1 == nry and nbx == nrx: break
                        if arr[nby+1][nbx] == 'O':
                            pos = 0
                            break
                        nby += 1
                else:
                    while 1:
                        if nby+1 < 1 or nby+1 >= N-1: break
                        if arr[nby+1][nbx] == '#': break
                        if arr[nby+1][nbx] == 'O':
                            pos = 0
                            break
                        nby += 1
                    while 1:
                        if nry+1 < 1 or nry+1 >= N-1: break
                        if arr[nry+1][nrx] == '#': break
                        if nry+1 == nby and nbx == nrx: break
                        if arr[nry+1][nrx] == 'O':
                            ans = cnt+1
                            nry = 0
                            break
                        nry += 1
            if pos:
                if ans:
                    return ans
                if nry != ry or nrx != rx or nby != by or nbx != bx:
                    move = {'R': (nry, nrx), 'B': (nby, nbx), 'cnt': cnt+1}
                    q.append(move)
            else:
                ans = 0
    return -1

print(abc())
