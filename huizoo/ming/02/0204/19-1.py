arr = [
    [3,5,4],
    [1,1,2],
    [1,3,9],
]

y, x = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

total = 0

for i in range(4) : 
    ny, nx = y + dy[i], x + dx[i]
    if 0 <= ny < 3 and 0 <= nx < 3 : 
        total += arr[ny][nx]

print(total)