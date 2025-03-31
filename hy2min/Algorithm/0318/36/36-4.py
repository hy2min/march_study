import heapq


c, p, k, a, b = map(int, input().split())  # 간선, 정점, 출발점, 방문점1, 방문점2

# 정점이 1부터 시작
arr = [[] for _ in range(p+1)]

for _ in range(c):
    p1, p2, d = map(int, input().split())
    arr[p1].append((p2, d))
    arr[p2].append((p1, d))  # 양방향 길이기 때문에 출발지 기준, 도착지 기준 둘다 추가

    inf = 21e8

def djikstra(start,end1,end2):
    result = [inf] * (p+1)
    result[start] = 0

    heap = [(0, start)]  # 거리가 우선순위로 빠짐 - 거리, 도착지점

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
    return result[end1] + result[end2]

ans = min(djikstra(a,k,b), djikstra(b,k,a))
print(ans)
# case1
# 방문점1 - 시작점
# 방문점1 - 방문점2
# start = a
# result[k]
# result[b]


# case2
# 방문점2 - 시작점
# 방문점2 - 방문점1
# start = b
# result[k]
# result[a]
# case1 vs case2