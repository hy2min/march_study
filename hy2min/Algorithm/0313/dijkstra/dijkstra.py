import heapq

# 5 7
# 0 1 3
# 0 3 9
# 0 4 5
# 1 2 7
# 1 4 1
# 2 3 1
# 4 2 1
# 0 3


n, m = map(int, input().split())

arr = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
start, end = map(int, input().split())

inf = 21e8
result = [inf] * n

heap = [(0,start)]  # 가중치, 인덱스
result[start] = 0

while heap:
    ky_cost, ky = heapq.heappop(heap)

    if result[ky] < ky_cost:
        continue
    for last, last_cost in arr[ky]:
         baro = result[last]
         new = ky_cost + last_cost

         if baro > new:
            result[last] = new
            heapq.heappush(heap,(new, last))

print(result[end]

