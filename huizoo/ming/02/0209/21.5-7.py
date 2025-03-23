arr = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 'W', 0, 'W', 0, 0],
    [0, 'W', 'B', 0, 'B', 'W', 0,],
    [0, 0, 'W', 'B', 'W', 0, 0],
    [0, 0, 'B', 'W', 0, 'W', 0,],
    [0, 'W', 'W', 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

input_y, input_x = map(int, input().split())

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
catch = 0
for i in range(4) : 
    ny, nx = input_y + dy[i], input_x + dx[i]
    if 0 <= ny < 7 and 0 <= nx < 7 and arr[ny][nx] == 'B' :
        cnt = 0
        for j in range(4) : 
            ny2, nx2 = ny+dy[i], nx+dx[i]
            if 0 <= ny < 7 and 0 <= nx < 7 and arr[ny2][nx2] == 'W' :
                cnt += 1
        if cnt == 4 : 
            catch += 1

print(catch)