import heapq

n = int(input())
maxheap, minheap = [], []

heapq.heappush(maxheap, -500)

for _ in range(n):
    mid = -heapq.heappop(maxheap)

    a, b = map(int, input().split())
    heapq.heappush(maxheap, -mid)
    if a > mid:
        heapq.heappush(minheap, a)
    else:
        heapq.heappush(maxheap, -a)

    if b > mid:
        heapq.heappush(minheap, b)
    else:
        heapq.heappush(maxheap, -b)

    while True:

        if len(minheap) > len(maxheap):
            heapq.heappush(maxheap, -heapq.heappop(minheap))
            if len(maxheap) - len(minheap) == 1:
                break
        if len(maxheap) > len(minheap):
            heapq.heappush(minheap, -heapq.heappop(maxheap))
            if len(maxheap) - len(minheap) == 1:
                break

    print(-maxheap[0])