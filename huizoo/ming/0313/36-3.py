import heapq

def dijkstra(graph, start, n):
    INF = float('inf')
    distance = [INF] * (n + 1)
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distance[node]:
            continue

        for neighbor, cost in graph[node]:
            new_dist = dist + cost
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distance


def solve(n, p, roads):
    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]

    for u, v, w in roads:
        graph[u].append((v, w))
        reverse_graph[v].append((u, w))

    # 1. 모든 마을 -> P 마을 최단 거리
    to_p = dijkstra(graph, p, n)

    # 2. P 마을 -> 모든 마을 최단 거리
    from_p = dijkstra(reverse_graph, p, n)

    # 3. 가장 오래 걸리는 학생 찾기
    max_time = 0
    for i in range(1, n + 1):
        if to_p[i] != float('inf') and from_p[i] != float('inf'):
            max_time = max(max_time, to_p[i] + from_p[i])

    return max_time


# 입력 예제
n, m, p = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

print(solve(n, p, arr))