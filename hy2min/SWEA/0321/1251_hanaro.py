import heapq
def prim(tax):
    pq = [(0,0)]  # (비용, 노드)
    visited = [0] *n  # 방문 여부 기록
    min_cost = 0  # 최소 비용

    dists = [float('inf')] * n
    dists[0] = 0

    while pq:
        cost, node = heapq.heappop(pq)

        if visited[node]:
            continue

        # node로 가는 간선을 확정짓는 코드
        visited[node] = 1
        min_cost += cost

        for next_node in range(n):
            if visited[next_node]:
                continue

            new_cost = ((x_list[next_node] - x_list[node])**2+(y_list[next_node] - y_list[node])**2) * tax

            if new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    return round(min_cost)
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())

    result = prim(tax)
    print(f'#{tc} {result}')