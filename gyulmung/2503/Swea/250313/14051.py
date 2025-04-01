import sys
sys.stdin = open('input.txt','r')

from collections import deque
T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    q = deque()

    for i in arr:
        q.append(i)

    for i in range(M):
        a = q.popleft()
        q.append(a)

    print(f'#{test} {q[0]}')