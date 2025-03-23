# 버스 환승
import sys
from collections import deque
input = sys.stdin.readline


M, N = map(int, input().split())
K = int(input())

buses = [set() for _ in range(K+1)]
stations = dict()

for _ in range(K):
    b, x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            station = (x1, y)
            if station not in stations:
                stations[station] = []
            stations[station].append(b)
    else:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            station = (x, y1)
            if station not in stations:
                stations[station] = []
            stations[station].append(b)

for bus in stations.values():
    for i in range(len(bus)-1):
        for j in range(i+1, len(bus)):
            a, b = bus[i], bus[j]
            buses[a].add(b)
            buses[b].add(a)

sx, sy, dx, dy = map(int, input().split())
start = (sx, sy)
end = (dx, dy)

def bfs():
    q = deque()
    visited = [0]*(K+1)
    for bus in stations.get(start, []):
        q.append(bus)
        visited[bus] = 1

    target = set(stations.get(end, []))
    if not target:
        return -1

    while q:
        now = q.popleft()
        for nxt in buses[now]:
            if nxt in target:
                return visited[now] + 1
            if visited[nxt] == 0:
                visited[nxt] = visited[now] + 1
                q.append(nxt)

    return -1
print(bfs())
