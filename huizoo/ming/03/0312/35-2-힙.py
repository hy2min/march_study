import heapq
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
heap = []
for i in range(n):
    for j in range(n):
        heapq.heappush(heap, (-arr[i][j], chr(i+65), chr(j+65)))

for _ in range(3):
    high = heapq.heappop(heap)
    print(f'{high[1]}-{high[2]} {-high[0]}')