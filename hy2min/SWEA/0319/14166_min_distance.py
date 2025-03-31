import heapq

inf = 21e8

t = int(input())
for tc in range(1, t+1):
    n, e = map(int, input().split())

    arr = [[] for _ in range(n+1)]
    for _ in range(e):
        s, e, w = map(int, input().split())
        arr[s].append((e, w))

    result = [inf] * (n+1)
    result[0] = 0
    heap = [(0,0)]

    while heap:
        ky_cost, ky = heapq.heappop(heap)

        if result[ky] < ky_cost:
            continue
        for dochack, dochack_cost in arr[ky]:
            baro = result[dochack]
            new = ky_cost + dochack_cost

            if baro > new:
                result[dochack] = new
                heapq.heappush(heap,(new, dochack))

    print(f'#{tc} {result[n]}')