import sys
sys.stdin = open('input.txt','r')

from collections import deque
T = int(input())

for test in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    lst = [[0]*(E+2) for _ in range((E+2))]
    for i in range(E):
        lst[arr[2*i]][arr[2*i+1]] = 1
    q = deque()
    q.append(N)
    cnt = 1
    while 1:
        y = q.popleft()
        for i in range(len(lst)):
            if lst[y][i] == 1:
                cnt += 1
                q.append(i)
        if not q:
            ret = cnt
            break
    print(f'#{test} {ret}')
