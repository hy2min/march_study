Y, X = map(int, input().split())
arr = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 'W', 0, 'W', 0, 0],
    [0, 'W', 'B', 0, 'B', 'W', 0],
    [0, 0, 'W', 'B', 'W', 0, 0],
    [0, 0, 'B', 'W', 0, 'W', 0],
    [0, 'W', 'W', 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
arr[Y][X] = 'W'
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
catch=0
for y in range(1,6):
    for x in range(1,6):
        if arr[y][x] == 'B':
            cnt = 0
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if arr[ny][nx] == 'W':
                    cnt+=1
            if cnt == 4:
                catch+=1

print(catch)