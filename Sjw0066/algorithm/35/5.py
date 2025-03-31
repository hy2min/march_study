import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write
N=int(input().rstrip())

middle=500
max_heap=[500]
min_heap=[]


for i in range(N):
    a,b = map(int,input().rstrip().split())
    if a>=middle:
        heapq.heappush(max_heap,a)
    else:
        heapq.heappush(min_heap,-a)

    if b>=middle:
        heapq.heappush(max_heap,b)
    else:
        heapq.heappush(min_heap,-b)

    while 1:
        if len(max_heap)==len(min_heap)+1:break
        if len(max_heap)>len(min_heap):
            heapq.heappush(min_heap,-heapq.heappop(max_heap))
        else:
            heapq.heappush(max_heap,-heapq.heappop(min_heap))

    middle=max_heap[0]

    print("%d\n" % middle)

