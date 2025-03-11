# import sys
# sys.stdin = open("input.txt","r")
from collections import deque

N = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)
Max = -21e8
q = deque()
q.append((0,0))

while q:
    now,score = q.popleft()
    if now == N:
        Max = max(score,Max)
    else:
        if now + 2 <= N:
            q.append((now+2,score+arr[now+2]))
        else:
            q.append((N,score))

        if now + 7 <= N:
            q.append((now+7,score+arr[now+7]))
        else:
            q.append((N,score))

print(Max)