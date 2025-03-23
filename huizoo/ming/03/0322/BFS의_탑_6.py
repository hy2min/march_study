# 결혼 정보 회사
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
T = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(T):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

COCO = int(input())
TARGET = int(input())

def bfs():
    q = deque([COCO])
    visited = [0]*(N+1)
    visited[COCO] = 1
    while q:
        friend = q.popleft()
        for i in arr[friend]:
            if visited[i] == 0:
                if i == TARGET:
                    return 'YES'
                visited[i] = 1
                q.append(i)

    return 'NO'


print(bfs())