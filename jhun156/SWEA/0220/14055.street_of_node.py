# import sys
# sys.stdin = open("input.txt","r")
from collections import deque

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(E)]
    connect_lst = [[] for _ in range(V+1)]
    for i in range(E):
        connect_lst[arr[i][0]].append(arr[i][1])
        connect_lst[arr[i][1]].append(arr[i][0])

    S,G = map(int,input().split())
    q = deque()
    visited = [0] * (V+1)
    visited[S] = 1
    q.append((S,0))
    Min = 0

    while q:
        now,level = q.popleft()
        if now == G:
            Min = level
            break

        for i in connect_lst[now]:
            if visited[i] == 0:
                visited[i] = 1
                q.append((i,level+1))

    print(f"#{tc} {Min}")