import sys
sys.stdin = open("input.txt", "r")


def put(y, x, color):
    global cnt1, cnt2
    board[y][x] = color
    for dy, dx in d:
        cnt = 0
        change = []
        for power in range(1, N):
            ny, nx = y + dy * power, x + dx * power
            if ny < 0 or nx < 0 or ny >= N or nx >= N: break
            if not board[ny][nx]: break
            if board[ny][nx] == color:
                if color == 1:
                    cnt2 -= cnt
                    cnt1 += cnt
                else:
                    cnt2 += cnt
                    cnt1 -= cnt
                if cnt:
                    for y1, x1 in change:
                        board[y1][x1] = color
                break
            change.append((ny, nx))
            cnt += 1

d = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
T = int(input())
for tc in range(1, T+1):
    # N = 보드 크기(4, 6, 8) M = 돌 놓는 횟수
    N, M = map(int, input().split())

    board = [[0]*N for _ in range(N)]
    for i in range(2):
        for j in range(2):
            board[N//2-i][N//2-j] = 2 if (i+j) % 2 == 0 else 1

    cnt1, cnt2 = 2, 2

    arr = [list(map(int, input().split())) for _ in range(M)]
    for i in range(M):
        # c = 1 : 흑돌 / 2 : 백돌
        a, b, c = arr[i]
        if c == 1: cnt1 += 1
        else: cnt2 += 1
        put(b-1, a-1, c)

    print(f'#{tc}', cnt1, cnt2)