import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    st = [] # start 포인트 위치 인자
    for i in range(N-1, -1, -1): #조건에 마지막 줄에 출발점이 있다했으므로 밑줄 탐색부터 시작
        if st: break # start 위치 인자가 있을 시 탐색 중지
        for j in range(N):
            if arr[i][j] == 2:
                st.append(i)
                st.append(j) #st에 시작지점 삽입
    ret = 0
    q = deque()
    q.append((st[0], st[1], 0))#실전에서 함수로 풀어낼것!!!!!
    while q:
        y, x, cnt = q.popleft()
        direct_Y = [0, 0, 1, -1]
        direct_X = [1, -1, 0, 0]
        for i in range(4):
            dy = direct_Y[i] + y
            dx = direct_X[i] + x
            if dy < 0 or dx < 0 or dy >= N or dx >= N: continue
            if arr[dy][dx] == 1: continue
            if arr[dy][dx] == 3:
                ret = cnt
            q.append((dy, dx, cnt+1))
            arr[dy][dx] = 1
        if ret:break # ret에 값이 있다면 stop

    print(f'#{test} {ret}')