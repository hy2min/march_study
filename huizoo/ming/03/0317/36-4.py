import heapq

# C : 길의 개수, P : 건물의 개수, K : 코코의 건물 위치
# 건물 번호 A, B
C, P, K, A, B = map(int, input().split())

arr = [[] for _ in range(P+1)]
# 1-based index
for _ in range(C):
    P1, P2, D = map(int, input().split())
    arr[P1].append((P2, D))
    arr[P2].append((P1, D))

def dijkstra(x):
    heap = [(0, x)]
    result = [1e9]*(P+1)

    while heap:
        now_cost, now = heapq.heappop(heap)
        for arrive, arrive_cost in arr[now]:
            straight = result[arrive]
            via = now_cost + arrive_cost
            if via < straight:
                result[arrive] = via
                heapq.heappush(heap, (via, arrive))

    return result

start = dijkstra(K)
via_A = dijkstra(A)
via_B = dijkstra(B)

print(min(start[A] + via_A[B], start[B] + via_B[A]))