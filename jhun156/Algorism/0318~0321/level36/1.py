# import sys
# sys.stdin = open("input.txt","r")
import heapq

N,M = map(int,input().split())
adj_lst = [[] for _ in range(N)]
for _ in range(M):
    index,goal,price = map(int,input().split())
    adj_lst[index].append((goal,price))     # 인접리스트에 시작노드에 도착노드,비용 입력
result = [21e8] * N
result[0] = 0
heap = []
heapq.heappush(heap,(0,0))

while heap:

    ky_cost, ky_index = heapq.heappop(heap)

    if result[ky_index] < ky_cost:
        continue

    for goal,cost in adj_lst[ky_index]:
        straight = result[goal]
        curve = ky_cost + cost
        if curve < straight:
            result[goal] = curve
            heapq.heappush(heap,(curve,goal))

if result[N-1] == 21e8:
    print("impossible")
else:
    print(result[N-1])