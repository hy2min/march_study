arr = [list(map(int, input().split())) for _ in range(7)]

d = [(-1, 0), (-1, -1), (-1, 1)]

dp = [[-1e9]*3 for _ in range(7)]
dp[0][0] = arr[0][0]

for y in range(1, 7):
    for x in range(3):
        if arr[y][x] == 0: continue
        for dy, dx in d:
            ny, nx = dy+y, dx+x
            if nx<0 or nx>=3: continue
            if dp[ny][nx] == -1e9: continue
            dp[y][x] = max(dp[y][x], dp[ny][nx] + arr[y][x])

print(max(dp[6]))