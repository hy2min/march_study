import sys
input = sys.stdin.readline

N = int(input()) # 보드 크기
K = int(input()) # 사과 개수
apples = []
for _ in range(K):
    i, j = map(int, input().split())
    apples.append((i-1, j-1)) # 사과 위치 1-based index 에서 0-based index 로 변환
direction = []
L = int(input()) # 방향 전환 횟수
for _ in range(L):
    t, d = input().split()
    direction.append((int(t), d))

direction.append((100, None)) # 어차피 100번 이동하면 벽을 만나기 때문에 방향 필요 없음

def abc():
    time = 0 # 시간 체크
    direct = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동쪽부터 시계방향
    look = 0 # 바라보고 있는 방향 direct[look]
    y = x = 0
    snake = [(0, 0)]
    for turn_time, turn in direction:
        dy, dx = direct[look] # 바라보고 있는 방향의 좌표
        for _ in range(turn_time - time): # 초만큼 이동
            time += 1
            ny, nx = y+dy, x+dx
            if ny<0 or nx<0 or ny>=N or nx>=N:
                return time # 이 때 시간을 계산해야함
            if (ny, nx) in snake:
                return time # 이 때도 반환 가능
            snake.append((ny, nx))
            if (ny, nx) in apples:
                apples.remove((ny, nx))
            else:
                snake.pop(0)
            y, x = ny, nx
        if turn == 'D':
            look = (look + 1) % 4
        elif turn == 'L':
            look = (look - 1) % 4


print(abc())

