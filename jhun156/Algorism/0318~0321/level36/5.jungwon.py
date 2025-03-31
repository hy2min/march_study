import heapq

def find_house(st_y, st_x):
    arr = [[INF] * N for _ in range(N)]
    arr[st_y][st_x] = 0
    pq = [(town[st_y][st_x], st_y, st_x)]

    while pq:
        tired, y, x = heapq.heappop(pq)

        if tired < arr[y][x]:
            continue

        next_axis = [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]
        next_axis = [a for a in next_axis if 0 <= a[0] < N and 0 <= a[1] < N]
        for next_y, next_x in next_axis:
            if town[next_y][next_x] == -1:
                continue
            new_tired = tired + town[next_y][next_x]
            if new_tired < arr[next_y][next_x]:
                arr[next_y][next_x] = new_tired
                heapq.heappush(pq, (new_tired, next_y, next_x))

    return arr

Y, X = map(int, input().split())
N = int(input())
town = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')
res = find_house(Y, X)
ans = 0

for lst in res:
    for n in lst:
        if n != INF:
            ans = max(n, ans)

print(ans)