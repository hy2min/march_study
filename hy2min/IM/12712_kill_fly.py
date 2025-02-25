def cross_kill(y, x):
    kill = arr[y][x]
    d_y = [-1,1,0,0]
    d_x = [0,0,-1,1]
    for i in range(4):
        for power in range(1, M):
            dy = y + d_y[i] * power
            dx = x + d_x[i] * power
            if dy < 0 or dx < 0 or dy > N-1 or dx > N-1:
                continue
            kill += arr[dy][dx]
    return kill

def x_kill(y, x):
    kill2 = arr[y][x]
    d_y = [-1,-1,1,1]
    d_x = [-1,1,-1,1]
    for i in range(4):
        for power in range(1, M):
            dy = y + d_y[i] * power
            dx = x + d_x[i] * power
            if dy < 0 or dx < 0 or dy > N-1 or dx > N-1:
                continue
            kill2 += arr[dy][dx]
    return kill2

T = int(input())
for idx in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_kill = float('-inf')

    for y in range(N):
        for x in range(N):

            total_kill = max(cross_kill(y, x), x_kill(y, x))

            if max_kill < total_kill:
                max_kill = total_kill

    print(f'#{idx+1} {max_kill}')