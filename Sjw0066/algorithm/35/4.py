import heapq
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
heap=[]

for i in range(N):
    for j in range(i,N):
        if arr[i][j]>0 :
            heapq.heappush(heap,arr[i][j])

for i in range(10):
    price=heapq.heappop(heap)
    cprice= price * 2
    heapq.heappush(heap,cprice)

print(f'{cprice}만원')
