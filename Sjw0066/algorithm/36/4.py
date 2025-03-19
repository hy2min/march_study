import heapq
C,P,K,A,B=map(int,input().split())

arr=[[] for _ in range(P)]
st=K-1
target1=A-1
target2=B-1

for i in range(C):
    p1,p2,D = map(int,input().split())
    arr[p1-1].append((p2-1,D))
    arr[p2-1].append((p1-1,D))

heap1=[]
heap2=[]

heapq.heappush(heap1,(0,st))
heapq.heappush(heap2,(0,target1))

result1=[21e8]*P
result2=[21e8]*P

result1[st]=0
result2[target1]=0

while heap1:
    ky_cost,ky=heapq.heappop(heap1)

    if result1[ky]<ky_cost:continue

    for i in range(len(arr[ky])):
        cango=arr[ky][i][0]
        cost=arr[ky][i][1]

        baro=result1[cango]
        new=ky_cost+cost

        if new<baro:
            result1[cango]=new
            heapq.heappush(heap1,(new,cango))

while heap2:
    ky_cost,ky=heapq.heappop(heap2)

    if result2[ky]<ky_cost:continue

    for i in range(len(arr[ky])):
        cango=arr[ky][i][0]
        cost=arr[ky][i][1]

        baro=result2[cango]
        new=ky_cost+cost

        if new<baro:
            result2[cango]=new
            heapq.heappush(heap2,(new,cango))

ans=min(result1[target1],result1[target2])+result2[target2]
print(ans)