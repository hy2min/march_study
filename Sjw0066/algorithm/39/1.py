import heapq
lst=list(map(int,input().split()))
heapq.heapify(lst)

time=0
ans=0
while len(lst)>1:
    time+=heapq.heappop(lst)
    ans+=time
print(ans)