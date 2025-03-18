import heapq


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

heap = []

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 and i != j:
            heapq.heappush(heap, (-arr[i][j], i, j))
ans = []
for _ in range(3):
    value, i, j = heapq.heappop(heap)
    ans.append((-value, chr(i+65), chr(j+65)))

for i in range(3):
    print(f'{ans[i][1]}-{ans[i][2]} {ans[i][0]}')