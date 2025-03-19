import sys
import heapq
sys.stdin = open("input.txt", "r")

T = int(input())
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 연료 소비량, y좌표, x좌표
    checked =[[1e9]*N for _ in range(N)]
    heap = [(0, 0, 0)]
    checked[0][0] = 0
    while heap:
        fuel, y, x = heapq.heappop(heap)
        if checked[y][x] < fuel:
            continue
        if y == x == N-1:
            print(f'#{tc} {fuel}')
            break
        for dy, dx in d:
            ny, nx = dy+y, dx+x
            if ny<0 or nx<0 or ny>=N or nx>=N: continue
            nxt_fuel = fuel + 1 + max(arr[ny][nx] - arr[y][x], 0)
            if checked[ny][nx] <= nxt_fuel:
                continue
            checked[ny][nx] = nxt_fuel
            heapq.heappush(heap, (nxt_fuel, ny, nx))






    # for i in range(N):
    #     for j in range(N):
    #         if i == 0 and j == 0: continue
    #         if i == 0:
    #             arr[i][j] = max(arr[i][j] - arr[i][j-1], 0) + arr[i][j-1]
    #         elif j == 0:
    #             arr[i][j] = max(arr[i][j] - arr[i-1][j], 0) + arr[i-1][j]
    #         else:
    #             arr[i][j] = max(arr[i][j] - arr[i-1][j], arr[i][j] - arr[i][j-1], 0) + min(arr[i-1][j], arr[i][j-1])
    #
    # print(f'#{tc} {arr[N-1][N-1] + 2*(N-1)}')
