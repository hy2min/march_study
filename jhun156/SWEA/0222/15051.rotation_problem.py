# import sys
# sys.stdin = open("input.txt","r")
from collections import deque

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    # N = 숫자 갯수, M = 반복횟수
    q = deque()
    arr = list(map(int,input().split()))
    for i in range(N):
        q.append(arr[i])

    cnt = 0
    while cnt < M:

        tmp = q.popleft()
        q.append(tmp)
        cnt += 1

    ans = q.popleft()
    print(f"#{tc} {ans}")