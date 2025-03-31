# 1.인접리스트로 받기
# 2.힙큐에 출발지와 비용(0) 집어넣기
# 3.result inf로 초기화
# 4.출발지 result 비용 0으로 만들기
# 5.힙에서 가져온 값을 출 -> 도로 놓고
# 경유지로 해당위치를 거칠때 최소 값들을 리절트 초기화
# 리절트가 힙에서 뺀 값보다 작으면 pass
# while heap

import heapq
N,M=map(int,input().split())
arr=[[] for _ in range(N)]
for i in range(M):
    a,b,c=map(int,input().split())
    arr[a].append((b,c))
heap=[]
result=[21e8]*N

heapq.heappush(heap,(0,0))
result[0]=0

while heap:
    ky_cost,ky=heapq.heappop(heap)

    if ky_cost>result[ky]:continue

    for i in range(len(arr[ky])):
        dochack=arr[ky][i][0]
        dochack_cost=arr[ky][i][1]

        if result[dochack] > ky_cost+dochack_cost:
            result[dochack] = ky_cost+dochack_cost
            heapq.heappush(heap,(ky_cost+dochack_cost,dochack))


if result[N-1] == 21e8:
    print('impossible')
else:
    print(result[N-1])



