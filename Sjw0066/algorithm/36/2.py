import heapq
N,M,K=map(int,input().split())
st,ed=map(int,input().split())
st-=1
ed-=1
arr=[[] for _ in range(N)]
for _ in range(M):
    f,t,c=map(int,input().split())
    arr[f-1].append([t-1,c])
    arr[t-1].append([f-1,c])

for k in range(K+1):
    if k>0:
        power = int(input())
        for i in arr:
            for j in i:
                j[1] += power

    heap = []
    heapq.heappush(heap, (0, st))
    result = [21e8] * N
    result[st] = 0

    while heap:
        ky_cost,ky=heapq.heappop(heap)

        if ky_cost>result[ky]:continue

        for i in range(len(arr[ky])):
            dochack=arr[ky][i][0]
            dochack_cost=arr[ky][i][1]

            baro=result[dochack]
            new=dochack_cost+ky_cost

            if baro>new:
                result[dochack]=new
                heapq.heappush(heap,(new,dochack))

    print(result[ed])





