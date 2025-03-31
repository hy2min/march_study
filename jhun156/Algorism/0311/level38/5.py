# import sys
# sys.stdin = open("input.txt","r")
from collections import deque

# 엘사는 멈추지 않고 8방향 이동
# 안나는 멈출수있고 4방향 이동 - 5개 디렉션
# 안나가 2칸 거리내에 있을땐 대각선 이동 x
# 절대값(안나x - 엘사x) <= 2 and 절대값(엘사y - 안나y) <= 2일때 대각선 x

N = int(input())
arr = [list(input()) for _ in range(N)]
visited_E = [[0] * N for _ in range(N)]
Ey,Ex,Ay,Ax = map(int,input().split())
visited_E[Ey][Ex] = 1

# 5방향
dy5 = [0,0,0,1,-1]
dx5 = [0,1,-1,0,0]

# 4방향
dy4 = [0,0,1,-1]
dx4 = [1,-1,0,0]

# 8방향
dy8 = [0,0,1,-1,1,1,-1,-1]
dx8 = [1,-1,0,0,1,-1,1,-1]
cnt = 0

def check(a,b,c,d):

    y = abs(a-b)
    x = abs(c-d)
    if x <= 2 and y <= 2:
        return 1

    return 0

Q = deque()
Q.append((Ay,Ax,Ey,Ex,0))
Min = 1000

while Q:

    Ay,Ax,Ey,Ex,cnt = Q.popleft()
    visited_E[Ey][Ex] = 1

    if Ay == Ey and Ax == Ex:
        Min = min(cnt,Min)

    check_direction = check(Ay,Ey,Ax,Ex)

    if check_direction:
        for i in range(5):
            dy1 = Ay + dy5[i]
            dx1 = Ax + dx5[i]
            if dy1 < 0 or dy1 > N - 1 or dx1 < 0 or dx1 > N - 1:    continue
            if arr[dy1][dx1] == '#':  continue

            for j in range(4):
                dy2 = Ey + dy4[j]
                dx2 = Ex + dx4[j]
                if dy2 < 0 or dy2 > N - 1 or dx2 < 0 or dx2 > N - 1:    continue
                if visited_E[dy2][dx2] == 1:  continue
                if arr[dy2][dx2] == '#':  continue
                Q.append((dy1,dx1,dy2,dx2,cnt+1))

    else:
        for i in range(5):
            dy1 = Ay + dy5[i]
            dx1 = Ax + dx5[i]
            if dy1 < 0 or dy1 > N - 1 or dx1 < 0 or dx1 > N - 1:    continue
            if arr[dy1][dx1] == '#':  continue

            for j in range(8):
                dy2 = Ey + dy8[j]
                dx2 = Ex + dx8[j]
                if dy2 < 0 or dy2 > N - 1 or dx2 < 0 or dx2 > N - 1:    continue
                if visited_E[dy2][dx2] == 1:  continue
                if arr[dy2][dx2] == '#':  continue
                Q.append((dy1,dx1,dy2,dx2,cnt+1))

print(f"{Min} sec")