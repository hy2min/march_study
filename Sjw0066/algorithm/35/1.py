import heapq



heap=list(map(lambda x:-ord(x),input()))
heapq.heapify(heap)

while heap:
    print(chr(-heapq.heappop(heap)),end="")
