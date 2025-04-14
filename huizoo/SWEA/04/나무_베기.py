import heapq
import sys
sys.stdin = open('input.txt', 'r')


def turn():
    for i in (-1, 1):
        if (sy, sx, (d + i) % 4) in visited: continue
        visited.add((sy, sx, (d + i) % 4))
        heapq.heappush(heap, (cnt + 1, k_cnt, (d + i) % 4, sy, sx))


DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
TT = int(input())
for tc in range(1, TT+1):
    N, K = map(int, input().split())
    arr = [input() for _ in range(N)]
    sy = sx = ey = ex = None
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                sy, sx = i, j
            elif arr[i][j] == 'Y':
                ey, ex = i, j
    visited = set()
    # 리모콘 조작 횟수, K 사용 횟수, 방향, 위치좌표 2개
    heap = [(0, 0, 0, sy, sx)]
    # 위치좌표, 리모콘 조작, T사용
    visited.add((sy, sx, 0))
    flag = 0
    while heap:
        cnt, k_cnt, d, sy, sx = heapq.heappop(heap)
        if sy == ey and sx == ex:
            print(f'#{tc} {cnt}')
            flag = 1
            break
        ny, nx = sy+DIR[d][0], sx+DIR[d][1]
        if ny<0 or nx<0 or ny>=N or nx>=N:
            turn()
        else:
            if arr[ny][nx] == 'T':
                if k_cnt < K:
                    if (ny, nx, d) not in visited:
                        visited.add((ny, nx, d))
                        heapq.heappush(heap, (cnt+1, k_cnt+1, d, ny, nx))
                        turn()
                else:
                    turn()
            else:
                if (ny, nx, d) not in visited:
                    visited.add((ny, nx, d))
                    heapq.heappush(heap, (cnt+1, k_cnt, d, ny, nx))
                    turn()
                else:
                    turn()

    if flag == 0:
        print(f'#{tc} -1')