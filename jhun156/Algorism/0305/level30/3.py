from collections import deque

arr = [
    [0,1,0,0,1,0],
    [0,0,1,0,0,1],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]
used = [0] * 6
a = int(input())
used[a] = 1
q = deque()
q.append(a)
while q:
    now = q.popleft()
    print(now,end=' ')
    for i in range(6):
        if arr[now][i] == 1 and used[i] == 0:
            used[i] = 1
            q.append(i)
