# import sys
# sys.stdin = open("input.txt","r")
import heapq

N, M, K, A, B = map(int,input().split())
# 길의 개수, 건물의 개수, 시작위치, 건물1, 건물2
adj_lst = [[] for _ in range(M+1)]
for _ in range(N):
    in1, in2, cost = map(int,input().split())
    adj_lst[in1].append([in2,cost])
    adj_lst[in2].append([in1,cost])


def dijkstra(st,ed):

    result = [21e8] * (M+1)
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

ref = dijkstra(A,B)
a = dijkstra(K,A) + ref
b = dijkstra(K,B) + ref
# 5 -> 4 and 4 -> 1
print(min(a,b))