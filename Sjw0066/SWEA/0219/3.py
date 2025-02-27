from collections import deque

T=int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    q=deque(map(int,input().split()))

    for i in range(M):
        q.append(q.popleft())

    print(f'#{tc} {list(q)[0]}')