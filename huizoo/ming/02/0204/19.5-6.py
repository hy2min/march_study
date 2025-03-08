map1 = [
    ['A', 'B', 'G', 'K'],
    ['T', 'T', 'A', 'B'],
    ['A', 'C', 'C', 'D'],
]

pattern = [list(input()) for _ in range(2)]
dy = [0, 0, 1, 1]
dx = [0, 1, 0, 1]
cnt = 0
for y in range(2) : 
    for x in range(3) :
        temp = 0 
        for i in range(4) : 
            ny, nx = y+dy[i], x+dx[i]
            if map1[ny][nx] == pattern[dy[i]][dx[i]] : 
                temp += 1
        if temp == 4 : 
            cnt += 1
if not cnt : 
    print('미발견')
else : 
    print(f'발견({cnt}개)')
