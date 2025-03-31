import heapq

from pprint import pprint

d_y = [-1,1,0,0]
d_x = [0,0,-1,1]


y, x = map(int, input().split())
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

inf = 21e8

def djikstra():
    path = [[inf]*n for _ in range(n)]
    path[y][x] = arr[y][x]
    heap = [(arr[y][x], y, x)]

    while heap:
        ky_cost, kyi, kyj = heapq.heappop(heap)

        if path[kyi][kyj] < ky_cost:
            continue
        for i in range(4):
            dy = kyi + d_y[i]
            dx = kyj + d_x[i]
            if dy < 0 or dx < 0 or dy >= n or dx >= n or arr[dy][dx] == -1:
                continue

            baro = path[dy][dx]
            new = ky_cost + arr[dy][dx]

            if baro > new:
                path[dy][dx] = new
                heapq.heappush(heap,(new,dy,dx))

    return path

path = djikstra()

for i in range(n):
     for j in range(n):
         if arr[i][j] == -1:
             path[i][j] = -1
mx = -21e8
for i in range(n):
    for j in range(n):
        if mx < path[i][j]:
            mx = path[i][j]

print(mx)