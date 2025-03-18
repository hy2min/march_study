arr = [
    [0,1,0,1,0],
    [1,2,0,2,1],
    [0,1,2,1,0],
    [0,2,1,0,1],
    [1,1,0,0,0]
]

y,x = map(int,input().split())

arr[y-1][x-1] = 1

cnt = 0
cnt2 = 0
for i in range(5):
    for j in range(5):
        if arr[i][j] == 2:
            for dy,dx in (0,1),(0,-1),(1,0),(-1,0):
                ny,nx = i+dy,j+dx
                if 0<=ny<5 and 0<=nx<5 and arr[ny][nx] == 1:
                    cnt += 1
            if cnt == 4:
                cnt2 += 1
                cnt = 0
            else:
                cnt = 0

print(cnt2)
