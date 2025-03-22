import heapq
# import sys
# sys.stdin = open("input.txt","r")

N, M, P = map(int,input().split())
adj_lst = [[] for _ in range(N+1)]
for _ in range(M):
    index, dochak, cost = map(int,input().split())
    adj_lst[index].append([dochak,cost])

def dijkstra(st,ed):

    result = [21e8] * (N+1)
    result[st] = 0
    heap = []
    heapq.heappush(heap, (0,st))

    while heap:

        ky_cost, ky = heapq.heappop(heap)

        if result[ky] < ky_cost:
            continue

        for goal, goal_cost in adj_lst[ky]:
            straight = result[goal]
            curve = ky_cost + goal_cost
            if straight > curve:
                result[goal] = curve
                heapq.heappush(heap, (curve,goal))

    return result[ed]

# P를 출발지로 하는 다익스트라 (1번만 하면 됨)

RESULT = [21e8] * (N+1)
RESULT[P] = 0
heap = []
heapq.heappush(heap, (0,P))

while heap:

    ky_cost, ky = heapq.heappop(heap)

    if RESULT[ky] < ky_cost:
        continue

    for goal, goal_cost in adj_lst[ky]:
        straight = RESULT[goal]
        curve = ky_cost + goal_cost
        if straight > curve:
            RESULT[goal] = curve
            heapq.heappush(heap, (curve,goal))


Max = -21e8
for i in range(1,N+1):
    if i == P:
        continue
    n1 = dijkstra(i,P)
    n2 = RESULT[i]
    if Max < n1+n2:
        Max = n1+n2

print(Max)