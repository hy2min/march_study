MAP = [list(input()) for _ in range(4)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
moved = []
for k in range(5):
    for y in range(4):
        for x in range(3):
            if MAP[y][x] == 'A' or MAP[y][x] == 'C' or MAP[y][x] == 'D':    
                moved.append(MAP[y][x])
                ny, nx = y + dy[k % 4], x + dx[k % 4]
                if 0 <= ny < 4 and 0 <= nx < 3:
                    if MAP[ny][nx] == '_':
                        MAP[y][x], MAP[ny][nx] = MAP[ny][nx], MAP[y][x]
                moved.pop()

print('\n'.join(''.join(row) for row in MAP))