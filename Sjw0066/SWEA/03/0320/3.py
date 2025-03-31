from collections import deque
# import sys
# sys.stdin = open("input.txt", "r")
T=int(input())

for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input())) for _ in range(N)]

    result=[[21e8]*N for _ in range(N)]
    q=deque()
    q.append((0,0,0))
    direct_y=[0,0,1,-1]
    direct_x=[1,-1,0,0]
    while q:
        y,x,now=q.popleft()
        if result[y][x] < now : continue
        for i in range(4):
            dy=direct_y[i]+y
            dx=direct_x[i]+x
            if dy<0 or dx<0 or dy>N-1 or dx>N-1 :continue
            next=now+arr[dy][dx]
            if result[dy][dx] >next:
                result[dy][dx] = next
                q.append((dy,dx,next))

    print(f'#{tc} {result[N - 1][N - 1]}')
