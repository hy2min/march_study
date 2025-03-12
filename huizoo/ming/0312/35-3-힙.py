import heapq
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
d = [(0, 1), (0, -1), (0, 0), (1, 0), (-1, 0)]
remains = n**2
heap = []
for i in range(n):
    for j in range(n):
        heapq.heappush(heap, (arr[i][j], i, j))

while remains:
    now, y, x = heapq.heappop(heap)
    if not arr[y][x]: continue
    cnt = now
    for dy, dx in d:
        ny, nx = y+dy, x+dx
        if ny<0 or nx<0 or ny>=n or nx>=n: continue
        if arr[ny][nx]:
            arr[ny][nx] = 0
            remains -= 1

print(f'{cnt}초')