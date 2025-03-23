import heapq
V, E = map(int, input().split())
arr = [[] for _ in range(V)]
min_costs = [float('inf')]*V
min_costs[0] = 0
pq = [(0, 0)]
for _ in range(E):
    u, v, cost = map(int, input().split())
    arr[u].append((cost, v))

def dijkstra():
    while pq:
        via_cost, via_idx = heapq.heappop(pq)
        if via_cost > min_costs[via_idx]:
            continue
        for nxt_cost, nxt in arr[via_idx]:
            via = via_cost + nxt_cost
            if via < min_costs[nxt]:
                min_costs[nxt] = via
                heapq.heappush(pq, (via, nxt))


dijkstra()

if min_costs[V-1] == float('inf'):
    print("impossible")
else:
    print(min_costs[V-1])