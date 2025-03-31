import heapq
dy = [-1,1,0,0]
dx = [0,0,-1,1]

inf = 21e8
def dijkstra():
    dists = [[inf] * n for _ in range(n)]
    dists[0][0] = 0

    heap = [(0, 0, 0)]  # 깊이,  y, x

    while heap:
        ky_cost, kyi, kyj = heapq.heappop(heap)

        if dists[kyi][kyj] < ky_cost:
            continue

        for i in range(4):
            new_y = kyi + dy[i]
            new_x = kyj + dx[i]
            if new_y < 0 or new_x < 0 or new_y >= n or new_x >= n:
                continue

            baro = dists[new_y][new_x]
            new = ky_cost + graph[new_y][new_x]

            if baro > new:
                dists[new_y][new_x] = new
                heapq.heappush(heap, (new, new_y, new_x))

    return dists[n-1][n-1]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]


    result = dijkstra()

    print(f'#{tc} {result}')
