import heapq
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
heap = []
for i in range(n):
    for j in range(i+1, n):
        if arr[i][j] > 0:
            heapq.heappush(heap, arr[i][j])

for i in range(10):
    x = 2*heapq.heappop(heap)
    heapq.heappush(heap, x)
    if i == 9:
        print(f'{x}만원')