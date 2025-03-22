import heapq

a = input()
heap = []
for i in range(len(a)):
    heapq.heappush(heap,(-ord(a[i]),ord(a[i])))

while heap:
    print(chr(heapq.heappop(heap)[1]),end='')