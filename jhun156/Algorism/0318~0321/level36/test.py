import sys
import heapq

sys.stdin = open("input.txt", "r")

N, M, K, A, B = map(int, input().split())

# 인접 리스트
adj_lst = [[] for _ in range(N + 1)]
for _ in range(M):
    in1, in2, cost = map(int, input().split())
    adj_lst[in1].append((in2, cost))
    adj_lst[in2].append((in1, cost))

def dijkstra(start, end):
    INF = float('inf')  # 무한대 값
    result = [INF] * (N + 1)
    result[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))  # (비용, 현재 노드)

    while heap:
        ky_cost, ky = heapq.heappop(heap)  # 현재 노드까지의 비용, 현재 노드

        # 이미 더 짧은 거리로 방문한 적 있다면 패스
        if result[ky] < ky_cost:
            continue

        for goal, goal_cost in adj_lst[ky]:
            new_cost = ky_cost + goal_cost  # 새로운 거리 계산

            if result[goal] > new_cost:
                result[goal] = new_cost  # 더 짧은 거리 갱신
                heapq.heappush(heap, (new_cost, goal))  # 힙에 추가

    return result[end] if result[end] != INF else float('inf')  # 도달할 수 없는 경우 무한대 반환

# K → A → B 경로
a = dijkstra(K, A) + dijkstra(A, B)
# K → B → A 경로
b = dijkstra(K, B) + dijkstra(B, A)

# 도달할 수 없는 경우 처리
answer = min(a, b)
print(answer if answer != float('inf') else -1)  # 도달할 수 없는 경우 -1 출력
