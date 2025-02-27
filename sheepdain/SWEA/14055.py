from collections import deque
 
def bfs(start):
    global ret
    q = deque()
    q.append((start, 0))
    used = [0] * (v+1)
    used[start] = 1
 
    while q:
        now = q.popleft()
        if now[0] == goal:
            ret = now[1]
            return
        for i in range(1, v + 1):
            if used[i]==0 and arr[now[0]][i] == 1:
                used[i]=1
                q.append((i, now[1] + 1))
 
T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    arr = [[0] * (v + 1) for _ in range(v + 1)]
    for i in range(e):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1
    start, goal = map(int, input().split())
    ret = 0
    bfs(start)
 
    print(f'#{test_case}', ret)
