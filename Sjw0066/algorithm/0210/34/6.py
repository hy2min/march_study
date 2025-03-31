import heapq

n=int(input())
heap=list(map(lambda x:(int(x),'G'),input().split()))
cnt=0
heapq.heapify(heap)
while heap:
    weight,stone=heapq.heappop(heap)

    if stone == 'S':
        break
    cnt += 1
    weight2,stone2=heapq.heappop(heap)

    if stone2=='S':
        break
    cnt += 1

    heapq.heappush(heap,(weight2*2,'S'))

print(cnt)

