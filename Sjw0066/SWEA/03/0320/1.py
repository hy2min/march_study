import heapq
T=int(input())

for tc in range(1,T+1):
    N,E=map(int,input().split())
    arr=[[] for _ in range(N+1)]

    for i in range(E):
        a,b,c=map(int,input().split())
        arr[a].append((b,c))

    result=[21e8]*(N+1)
    result[0] = 0
    heap=[]
    heapq.heappush(heap,(0,0))

    while heap:
        weight,node=heapq.heappop(heap)

        if result[node]<weight:continue


        for i in range(len(arr[node])):
            dochack=arr[node][i][0]
            dochack_cost=arr[node][i][1]

            baro=result[dochack]
            new=weight+dochack_cost

            if new<baro:
                result[dochack] = new
                heapq.heappush(heap,(new,dochack))


    ans=result[N]
    print(f'#{tc} {ans}')



