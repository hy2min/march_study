# import sys
# sys.stdin = open("input.txt","r")
import heapq

N, M, K = map(int,input().split())
start,end = map(int,input().split())    # 시작과 끝 인덱스
adj_lst = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj_lst[a].append([b, c])
    adj_lst[b].append([a, c])

k_lst = [0]
for i in range(K):
    k_lst.append(int(input()))

for i in range(K+1):
    if i != 0:
        for j in range(N+1):
            if adj_lst[j]:
                for arr in adj_lst[j]:
                    arr[-1] = arr[-1] + k_lst[i]
    heap = []
    result = [21e8] * (N + 1)
    result[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        ky_cost, ky = heapq.heappop(heap)
        if result[ky] < ky_cost:
            continue
        for goal, goal_cost in adj_lst[ky]:
            straight = result[goal]
            curve = ky_cost+goal_cost
            if straight > curve:
                result[goal] = curve
                heapq.heappush(heap, (curve, goal))

    print(result[end])