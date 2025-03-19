import heapq

def abc():
    heap = [(arr[Y][X], Y, X)]
    visited = [[0]*N for _ in range(N)]
    visited[Y][X] = 1
    while heap:
        fatigue, now_y, now_x = heapq.heappop(heap)
        for dy, dx in d:
            ny, nx = now_y + dy, now_x + dx
            if ny<0 or nx<0 or ny>=N or nx>=N: continue
            if arr[ny][nx] == -1: continue
            if visited[ny][nx]: continue
            if ny == y and nx == x:
                print(fatigue + Max)
                return
            visited[ny][nx] = 1
            heapq.heappush(heap, (fatigue + arr[ny][nx], ny, nx))

Y, X = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
Max = 0
y = x = -1
for i in range(N):
    for j in range(N):
        if arr[i][j] > Max:
            Max = arr[i][j]
            y, x = i, j

abc()
