import heapq, sys
input = sys.stdin.readline

def abc(p, lst):
    heap = [(0, p)]
    result = [21e8]*(N+1)
    result[p] = 0
    while heap:
        now_cost, now = heapq.heappop(heap)
        for arrive, arrive_cost in lst[now]:
            straight = result[arrive]
            via = now_cost + arrive_cost
            if via < straight:
                result[arrive] = via
                heapq.heappush(heap, (via, arrive))

    return result

N, M, P = map(int, input().split())

arr = [[] for _ in range(N+1)]
rev_arr = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, cost = map(int, input().split())
    arr[s].append((e, cost))
    rev_arr[e].append((s, cost))

ret1 = abc(P, arr)
ret2 = abc(P, rev_arr)

Max = 0

for i in range(1, N+1):
    if ret1[i] != 21e8 and ret2[i] != 21e8:
        Max = max(Max, ret1[i] + ret2[i])

print(ret1)
print(ret2)
print(Max)

