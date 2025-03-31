from collections import deque

T=int(input())

def bfs(st,level):
    global Min
    q=deque()
    q.append((st,level))
    visited=[0]*(V+1)
    visited[st]=1

    while q:
        now,cnt = q.popleft()

        if now == G:
            Min=min(Min,cnt)

        for i in arr[now]:
            if visited[i] == 1: continue
            visited[i] = 1
            q.append((i,cnt+1))




for tc in range(1,T+1):
    V,E = map(int,input().split())
    arr=[[] for _ in range(V+1)]

    for i in range(E):
        a,b=map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    S,G =map(int,input().split())
    Min=21e8
    bfs(S,0)
    if Min==21e8:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {Min}')

