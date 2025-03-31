# import sys
# sys.stdin = open("input.txt","r")
from collections import deque
from copy import deepcopy

sty,stx = map(int,input().split())
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
value = -10
edy,edx = -1,-1
for i in range(N):
    for j in range(N):
        if arr[i][j] > value:
            value = arr[i][j]
            edy, edx = i, j

# 출발지점부터 끝 지점까지 다익스트라 최소 코스트 구하기

q = deque()
visited = [[0] * N for _ in range(N)]
visited[sty][stx] = 1
q.append((sty,stx,arr[sty][stx],visited))
Min = 21e8
directY = [0,0,1,-1]
directX = [1,-1,0,0]

while q:
    ny,nx,Sum,lst = q.popleft()
    if ny == edy and nx == edx:
        Min = min(Min,Sum)

    for i in range(4):
        dy = ny + directY[i]
        dx = nx + directX[i]
        if dy < 0 or dx < 0 or dy > N - 1 or dx > N - 1:
            continue
        if lst[dy][dx] == 1:
            continue
        if arr[dy][dx] == -1:
            continue
        lst[dy][dx] = 1
        tmp_lst = deepcopy(lst)
        q.append((dy,dx,Sum+arr[dy][dx],tmp_lst))

print(Min)