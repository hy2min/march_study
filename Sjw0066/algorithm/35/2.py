import heapq

N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
name=list(map(lambda x:chr(x),range(65,65+N)))
heap=[]
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            heapq.heappush(heap,(-arr[i][j],i,j))

for i in range(3):
    price,st,ed=heapq.heappop(heap)
    print(f'{name[st]}-{name[ed]} {-price}')



