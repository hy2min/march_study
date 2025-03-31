from collections import deque

arr = [
    [0,0,0,0,1,0],
    [1,0,1,0,0,0],
    [1,0,0,1,0,0],
    [1,1,0,0,0,0],
    [0,1,0,1,0,1],
    [0,0,1,1,0,0],
]

a = int(input())
q = deque()
q.append(a)
used = [0] * 6
used[a] = 1

while q:
    now = q.popleft()
    print(now)
    for i in range(6):
        if arr[now][i] == 1 and used[i] == 0:
            used[i] = 1
            q.append(i)

