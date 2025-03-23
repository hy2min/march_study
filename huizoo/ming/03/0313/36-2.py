import heapq, copy

N, M, K = map(int, input().split())
A, B = map(int, input().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    f, t, c = map(int, input().split())
    arr[f].append((t, c))
    arr[t].append((f, c))
def find_min(lst):
    result = [21e8] * (N + 1)
    result[A] = 0
    heap = [(0, A)]
    while heap:
        cost, via = heapq.heappop(heap)
        if result[via] < cost:
            continue
        for nxt, nxt_cost in lst[via]:
            via_cost = cost + nxt_cost
            if via_cost < result[nxt]:
                result[nxt] = via_cost
                heapq.heappush(heap, (via_cost, nxt))
    print(result[B])
find_min(arr)
for _ in range(K):
    p = int(input())
    for i in range(len(arr)):
        if arr[i]:
            for j in range(len(arr[i])):
                arr[i][j] = (arr[i][j][0], arr[i][j][1]+p)
    find_min(arr)