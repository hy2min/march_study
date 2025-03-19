import heapq

# N = 도시의 수, M = 고속도로의 수, K = 해의 수
N, M, K = map(int, input().split())
# 도시 A, B
A, B = map(int, input().split())
# 0-based index 로 변환
A -= 1
B -= 1

arr = [[] for _ in range(N)]
for _ in range(M):
    f, t, cost = map(int, input().split())
    arr[f-1].append((t-1, cost))
    arr[t-1].append((f-1, cost))


def abc(x):
    for i in range(N):
        for j in range(len(arr[i])):
            arr[i][j] = (arr[i][j][0], arr[i][j][1] + x)

    heap = [(0, A)]
    result = [21e8]*N
    result[A] = 0
    while heap:
        now_cost, now = heapq.heappop(heap)
        for arrive, arrive_cost in arr[now]:
            straight = result[arrive]
            via = now_cost + arrive_cost
            if via < straight:
                result[arrive] = via
                heapq.heappush(heap, (via, arrive))

    return result[B]

print(abc(0))
for _ in range(K):
    p = int(input())
    print(abc(p))
