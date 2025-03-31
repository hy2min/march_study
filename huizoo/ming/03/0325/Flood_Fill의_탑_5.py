# 퀴즈 검수자
import sys
from collections import deque
input = sys.stdin.readline

d = [(-2, -3), (-3, -2), (-3, 2), (-2, 3), (2, -3), (3, -2), (3, 2), (2, 3)]


H, W = map(int, input().split())    # 장기판 크기
arr = [[-1]*W for _ in range(H)]

R, C = map(int, input().split())    # 붉은색 상
Y, X = map(int, input().split())    # 파란색 차
N = int(input())                    # 쫄 개수
for _ in range(N):                  # 쫄 위치
    y, x = map(int, input().split())
    arr[y][x] = -2

q = deque([(R, C)])
arr[R][C] = 0
while q:
    yy, xx = q.popleft()
    if yy == Y and xx == X:
        print(arr[Y][X])
        exit()
    for dy, dx in d:
        ny, nx = yy+dy, xx+dx
        if 0 <= ny < H and 0 <= nx < W:
            if arr[ny][nx] == -1:
                arr[ny][nx] = arr[yy][xx] + 1
                q.append((ny, nx))

print(-1)