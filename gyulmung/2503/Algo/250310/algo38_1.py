import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

s = int(input())
d = int(input())

q = deque()
q.append((s, 0))
visited = [0]*100001
visited[s] = 1

while q:
    x, cnt = q.popleft()

    if x == d:
        print(cnt)
        break

    moving = [x // 2, x - 1, x + 1, x * 2]
    for i in range(4):
        if 0 <= moving[i] <= 100000 and visited[moving[i]] != 1:
            visited[moving[i]] = 1
            q.append((moving[i], cnt + 1))

