import sys
sys.stdin = open("input.txt","r")
from collections import deque

N = int(input())
arr = [input() for _ in range(N)]
y1, x1, y2, x2 = map(int, input().split())
d1 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
d2 = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def move(y1, x1, y2, x2):
    visited = set()
    # visited1 = [[0]*N for _ in range(N)]
    visited.add((y1, x1, y2, x2))
    # visited1[y1][x1] = 1
    q = deque([(y1, x1, y2, x2, 0)])
    while q:
        yy1, xx1, yy2, xx2, time = q.popleft()
        # print(f"엘사: ({yy1}, {xx1}), 안나: ({yy2}, {xx2}), 시간: {time}")
        if yy1 == yy2 and xx1 == xx2: # 위치 같으면 걸린 시간 리턴
            return time
        if safe(yy1, xx1, yy2, xx2):  # 마법으로부터 안전할 때 (대각선 이동 가능)
            move_elsa = d2
        else:  # 위험할 때 (4방향 이동만 가능)
            move_elsa = d1 # 마법으로부터 안전할 때

        for dy1, dx1 in move_elsa: # 엘사 먼저
            ny1, nx1 = yy1+dy1, xx1+dx1
            if ny1<0 or nx1<0 or ny1>=N or nx1>=N: continue
            if arr[ny1][nx1] == '#': continue
            # if visited1[ny1][nx1]: continue
            # visited1[ny1][nx1] = 1

            for dy2, dx2 in d1: # 안나도 계산
                ny2, nx2 = yy2+dy2, xx2+dx2
                if ny2<0 or nx2<0 or ny2>=N or nx2>=N: continue
                if arr[ny2][nx2] == '#': continue
                if (ny1, nx1, ny2, nx2) in visited: continue
                visited.add((ny1, nx1, ny2, nx2))
                q.append((ny1, nx1, ny2, nx2, time+1))

            if (ny1, nx1, yy2, xx2) not in visited: # 제자리에 있는 경우도 계산
                visited.add((ny1, nx1, yy2, xx2))
                q.append((ny1, nx1, yy2, xx2, time + 1))

    return

def safe(y1, x1, y2, x2):
    if abs(y1 - y2) <= 2 and abs(x1 - x2) <= 2: return 0
    return 1


print(f'{move(y1, x1, y2, x2)} sec')