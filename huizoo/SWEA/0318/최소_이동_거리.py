import sys
import heapq
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    arr = [[] for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        arr[s].append((e, w))

    result = [1e9]*(N+1)
    result[0] = 0

    heap = [(0, 0)]
    while heap:
        now_cost, now = heapq.heappop(heap)
        for arrive, arrive_cost in arr[now]:
            straight = result[arrive]
            via = now_cost + arrive_cost
            if via < straight:
                result[arrive] = via
                heapq.heappush(heap, (via, arrive))

    print(f'#{tc} {result[N]}')