import heapq
arr = list(input())
heap = []
for i in arr:
    heapq.heappush(heap, -ord(i))
for i in range(len(heap)):
    print(chr(-heapq.heappop(heap)), end='')