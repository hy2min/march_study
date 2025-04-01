import sys
sys.stdin = open('input.txt','r')

from collections import deque
T = int(input())

for test in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    q = deque()
    for i in range(N):
        q.append((arr[i], i))
        cnt += 1
    while 1:
        if len(q) == 1:
            break
        ch, idx = q.popleft()
        if ch // 2 != 0:
            q.append((ch//2, idx))
        else:
            if cnt == M: continue
            q.append((arr[cnt], cnt))
            cnt+=1

    print(f'#{test} {q[0][1] + 1}')
