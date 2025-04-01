import sys
sys.stdin = open('input.txt','r')

from collections import deque


def bfs(start):
    q = deque([(start, 0)])
    visited[start] = True

    while q:
        node, dist = q.popleft()
        if node == G:
            return dist

        for i in range(N):
            if arr[node][i] == 1 and not visited[i]:
                visited[i] = True
                q.append((i, dist + 1))

    return 0


T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]

    for _ in range(M):
        y, x = map(int, input().split())
        arr[y - 1][x - 1] = 1
        arr[x - 1][y - 1] = 1

    S, G = map(int, input().split())
    S -= 1
    G -= 1

    visited = [False] * N
    result = bfs(S)

    print(f'#{test} {result}')