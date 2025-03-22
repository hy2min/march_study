import heapq

N = int(input())
heap = []
arr = list(map(int,input().split()))
for i in range(N):
    heapq.heappush(heap,(arr[i],'G'))

cnt = 0
while 1:

    a = heapq.heappop(heap)
    if a[1] == 'S':
        break
    else:
        cnt += 1
    b = heapq.heappop(heap)
    if b[1] == 'S':
        break
    else:
        cnt += 1
        heapq.heappush(heap,(2*b[0], 'S'))

print(cnt)