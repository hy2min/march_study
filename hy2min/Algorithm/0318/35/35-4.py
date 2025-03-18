import heapq

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

heap = []
for i in range(n):
    for j in range(i, n):
        if arr[i][j] > 0 and i != j:
            heapq.heappush(heap, (arr[i][j], i, j))

for i in range(10):
    cost, y, x = heapq.heappop(heap)
    heapq.heappush(heap, (cost*2, y, x))

print(f'{cost*2}만원')