import heapq
n = int(input())
left = []
right = []
heapq.heappush(left, -500)
for _ in range(n):
    a, b = map(int, input().split())
    for i in (a, b):
        if i < -left[0]:
            heapq.heappush(left, -i)
        elif i >= -left[0]:
            heapq.heappush(right, i)
    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))
    print(-left[0])