# # import sys
# # sys.stdin = open("input.txt","r")
#
# def dfs(y,x,Sum):
#
#     global ans
#     if Sum > ans:
#         return
#
#     if y == x == N - 1:
#         ans = min(ans,Sum)
#         return
#
#     if y + 1 <= N - 1:
#         if arr[y+1][x] > arr[y][x]:
#             dfs(y+1,x,Sum+arr[y+1][x]-arr[y][x]+1)
#         else:
#             dfs(y+1,x,Sum+1)
#
#     if x + 1 <= N - 1:
#         if arr[y][x+1] > arr[y][x]:
#             dfs(y,x+1,Sum+arr[y][x+1]-arr[y][x]+1)
#         else:
#             dfs(y,x+1,Sum+1)
#
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#     ans = 21e8
#
#     dfs(0,0,0)
#     print(f"#{tc} {ans}")

import sys
sys.stdin = open("input.txt","r")
import heapq

def dijkstra(N):
    dist[0][0] = 0
    pq = [(0,0,0)]  # cost,y,x

    while pq:

        cost,y,x = heapq.heappop(pq)

        if dist[y][x] < cost:
            continue

        for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]:
            ny, nx = y + dy, x + dx

            if ny < 0 or ny > N - 1 or nx < 0 or nx > N - 1:
                continue
            if dist[ny][nx] > cost + max(0, arr[ny][nx] - arr[y][x]) + 1:
                dist[ny][nx] = cost + max(0, arr[ny][nx] - arr[y][x]) + 1
                heapq.heappush(pq, (cost + max(0, arr[ny][nx] - arr[y][x]) + 1, ny, nx))

    return dist[N-1][N-1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[21e8] * N for _ in range(N)]

    ans = dijkstra(N)
    print(f"#{tc} {ans}")