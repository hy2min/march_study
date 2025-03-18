import heapq
N,M,P = map(int,input().split())
P-=1
arr=[[] for _ in range(N)]

for _ in range(M):
    a,b,c=map(int,input().split())
    arr[a-1].append((b-1,c))

answer=[0]*N



for st in range(N):
    heap=[]
    heapq.heappush(heap,(0,st))
    result = [21e8] * N
    result[st] = 0

    # 1, 2, 3, 4 를 시작지로 다익스트라
    # st가 1,3,4 면 result의 2번을 answer의 st에 더하기
    # st가 2면 result의 1,3,4 를 answer의 1,3,4에 더하기

    while heap:
        ky_cost, ky = heapq.heappop(heap)

        if ky_cost > result[ky]: continue

        for i in range(len(arr[ky])):
            dochack = arr[ky][i][0]
            dochack_cost = arr[ky][i][1]

            baro = result[dochack]
            new = dochack_cost + ky_cost

            if baro > new:
                result[dochack] = new
                heapq.heappush(heap, (new, dochack))

    if st==P:
        for i in range(4):
            if i == P: continue
            answer[i] +=result[i]
    else:
        answer[st]+=result[P]


print(max(answer))














