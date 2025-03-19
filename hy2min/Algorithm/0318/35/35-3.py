import heapq

d_y = [-1,1,0,0]
d_x = [0,0,-1,1]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

heap = []
for i in range(n):
    for j in range(n):
        heapq.heappush(heap, (arr[i][j], i, j))


max_time = 0
while heap:
    time, i, j = heapq.heappop(heap)

    if arr[i][j] == -1:
        continue
    max_time = time
    arr[i][j] = -1
    for dn in range(4):
        dy = i + d_y[dn]
        dx = j + d_x[dn]
        if dy < 0 or dx < 0 or dy >= n or dx >= n:
            continue
        arr[dy][dx] = -1
print(f'{max_time}초')