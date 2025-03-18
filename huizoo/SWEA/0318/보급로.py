import heapq
import sys
sys.stdin = open("input.txt", "r")

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    dp = [[1e9]*N for _ in range(N)]
    # 현재 시간, y좌표, x좌표
    heap = [(0, 0, 0)]
    dp[0][0] = 0
    while heap:
        now, y, x = heapq.heappop(heap)
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if ny<0 or nx<0 or ny>=N or nx>=N: continue
            nxt = dp[y][x] + arr[ny][nx]
            if nxt >= dp[ny][nx]:
                continue
            dp[ny][nx] = dp[y][x] + arr[ny][nx]
            heapq.heappush(heap, (nxt, ny, nx))

    print(f'#{tc} {dp[N-1][N-1]}')