arr = [['_']*5 for _ in range(4)]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
for _ in range(2):
    y, x = map(int, input().split())
    for i in range(8):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<4 and 0<=nx<5:
            arr[ny][nx] = '#'

print('\n'.join(' '.join(row) for row in arr))