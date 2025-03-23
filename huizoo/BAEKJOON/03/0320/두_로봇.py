import heapq, sys
input = sys.stdin.readline

def dijkstra(x, lst):
    result = [1e9]*(N+1)
    result[x] = 0
    heap = [(0, x)]

    while heap:
        now_cost, now = heapq.heappop(heap)
        for arrive, arrive_cost in lst[now]:
            straight = result[arrive]
            via = now_cost + arrive_cost
            if via < straight:
                result[arrive] = via
                heapq.heappush(heap, (via, arrive))

    return result

N, r1, r2 = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N-1)]
arr2 = [[] for _ in range(N+1)]

if r1 == r2:
    print(0)
else:
    for a, b, cost in arr:
        arr2[a].append((b, cost))
        arr2[b].append((a, cost))

    ret1 = dijkstra(r1, arr2)
    ret2 = dijkstra(r2, arr2)

    Min = 1e9
    for room1, room2, temp in arr:
        Min = min(Min,
                  ret1[room1] + ret2[room2],
                  ret1[room2] + ret2[room1])

    print(Min)