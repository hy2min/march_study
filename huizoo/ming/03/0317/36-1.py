import heapq

N, T = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(T):
    u, v, cost = map(int, input().split())
    arr[u].append((v, cost))

start = 0
end = N-1
heap = [(0, start)]
result = [21e8]*N
result[start] = 0

while heap:
    now_cost, now = heapq.heappop(heap)
    if result[now] < now_cost: continue

    for arrive, arrive_cost in arr[now]:
        straight = result[arrive]
        via = arrive_cost + now_cost
        if straight > via:
            result[arrive] = via
            heapq.heappush(heap, (via, arrive))

if result[N-1] == 21e8:
    print('impossible')
else:
    print(result[N-1])