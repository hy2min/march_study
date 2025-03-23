# import sys
# sys.stdin = open("input.txt","r")
import heapq

T = int(input())
for tc in range(1,T+1):
    N, E = map(int,input().split())
    adj_lst = [[] for _ in range(N+1)]
    for i in range(E):
        a,b,c = map(int,input().split())
        adj_lst[a].append([b,c])    # b,c = index, cost
    heap = [(0,0)]
    result = [21e8] * (N+1)

    while heap:

        ky_cost,ky = heapq.heappop(heap)

        if result[ky] < ky_cost:
            continue

        for goal, goal_cost in adj_lst[ky]:
            straight = result[goal]
            curve = ky_cost + goal_cost
            if straight > curve:
                result[goal] = curve
                heapq.heappush(heap, (curve,goal))

    print(f"#{tc} {result[N]}")
