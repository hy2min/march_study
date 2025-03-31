# 알뜰 기차여행
import heapq, sys
input = sys.stdin.readline

N, T = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(T):
    a, b, w = map(int, input().split())
    arr[a].append((w, b))
result = [1e9]*N

heap = [(0, 0)]
while heap:
    now_weight, now = heapq.heappop(heap)
    for nxt_weight, nxt in arr[now]:
        straight = result[nxt]
        via = now_weight+nxt_weight
        if via < straight:
            result[nxt] = via
            heapq.heappush(heap, (via, nxt))

if result[N-1] == 1e9:
    print('impossible')
else:
    print(result[N-1])