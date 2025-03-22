# import sys
# sys.stdin = open("input.txt","r")
import heapq

N = int(input())
left = [-500]
right = []
for _ in range(N):
    a,b = map(int,input().split())
    if a >= -left[0]:
        heapq.heappush(right,a)
    else:
        heapq.heappush(left,-a)
    if b >= -left[0]:
        heapq.heappush(right,b)
    else:
        heapq.heappush(left,-b)

    while len(left) != len(right) + 1:
        if len(left) > len(right) + 1:
            heapq.heappush(right,-heapq.heappop(left))
        elif len(left) < len(right) + 1:
            heapq.heappush(left,-heapq.heappop(right))

    print(-left[0])