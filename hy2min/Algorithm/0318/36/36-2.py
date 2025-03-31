import heapq

n, m, k = map(int, input().split())  # 도시, 고속도로, 해(반복횟수)
arr = [[] for _ in range(n+1)]

a, b = map(int, input().split())  # start, end
for _ in range(m):
    f, t, c = map(int, input().split())  # 시작점, 도착점, 비용
    arr[f].append((t, c))


costs = [int(input()) for _ in range(k)]
inf = 21e8
result = [inf] * (n+1)

result[a] = 0
heap = [(0, a)]

for cost in costs:

    while heap:
        ky_cost, ky = heapq.heappop(heap)
        ky_cost += cost
        if result[ky] < ky_cost:
            continue

        for dochack, dochack_cost in arr[ky]:
            dochack_cost += cost
            direct = result[dochack]
            new = ky_cost + dochack_cost

            if direct > new:
                result[dochack] = new
                heapq.heappush(heap, (new, dochack))
    print(result[b])