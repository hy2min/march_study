input_list = [list(map(int, input().split())) for _ in range(5)]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
flag = 0
for y in range(5) : 
    for x in range(4) : 
        if input_list[y][x] :
            for i in range(8) : 
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < 5 and 0 <= nx < 4 : 
                    if input_list[ny][nx] :
                        flag = 1

if flag : 
    print('불안정한 상태')
else : 
    print('안정된 상태')