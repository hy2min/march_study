# import sys
# sys.stdin = open("input.txt","r")
from collections import deque

T = 10
for tc in range(1,T+1):
    t = int(input())
    n = 8
    arr = list(map(int,input().split()))
    q = deque()
    for i in arr:
        q.append(i)
    while 1:
        for i in range(1,6):
            tmp = q.popleft()
            if tmp - i <= 0:
                q.append(0)
                break
            else:
                q.append(tmp - i)
        if 0 in q:
            print(f"#{tc}",end=' ')
            print(*list(q))
            break