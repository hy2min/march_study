from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dat = [0]*(N+1)
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)

for i in range(1, N+1):
    for k in arr[i]:
        dat[k] += 1

q = deque()
for i in range(1, N+1):
    if dat[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    print(now, end=' ')
    for i in arr[now]:
        dat[i] -= 1
        if dat[i] == 0:
            q.append(i)