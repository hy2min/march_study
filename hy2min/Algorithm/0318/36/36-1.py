import heapq

n, t = map(int, input().split())

arr = [[] for _ in range(n)]

for _ in range(t):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
inf = 21e8
result = [inf] * n

# heap -> 가중치, 도착지 저장
heap = [(0, 0)]
result[0] = 0

while heap:
    ky_cost, ky = heapq.heappop(heap)
    if result[ky] < ky_cost:
        continue
    for dochack, dochack_cost in arr[ky]:
        baro = result[dochack]
        new = ky_cost + dochack_cost

        if baro > new:
            result[dochack] = new
            heapq.heappush(heap, (new, dochack))

if result[n-1] == inf:
    print('impossible')
else:
    print(result[n-1])