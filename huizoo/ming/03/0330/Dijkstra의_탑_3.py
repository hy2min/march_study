# N x M 최단 거리
import heapq, sys
input = sys.stdin.readline

def dijkstra():
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    heap = [(arr[0][0], 0, 0)]
    visited = [[1e9]*M for _ in range(N)]
    visited[0][0] = arr[0][0]
    while heap:
        w, y, x = heapq.heappop(heap)
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if ny<0 or nx<0 or ny>=N or nx>=M: continue
            if ny == N-1 and nx == M-1:
                return w+arr[ny][nx]
            if visited[ny][nx] > w+arr[ny][nx]:
                visited[ny][nx] = w+arr[ny][nx]
                heapq.heappush(heap, (w+arr[ny][nx], ny, nx))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(dijkstra())
