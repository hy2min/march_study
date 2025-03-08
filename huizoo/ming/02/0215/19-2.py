Map = [
    [3,3,5,3,1],
    [2,2,4,2,6],
    [4,9,2,3,4],
    [1,1,1,1,1],
    [3,3,5,9,2],
]
dy = [-1, -1, 1, 1]
dx = [-1, 1, -1, 1]
Max = -21e8
i, j = 0, 0
for y in range(5):
    for x in range(5):
        Sum = 0
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<5 and 0<=nx<5:
                Sum += Map[ny][nx]
        if Max < Sum:
            Max = Sum
            i, j = y, x
print(i, j)