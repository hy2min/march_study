Map = [
    ['A','B','G','K'],
    ['T','T','A','B'],
    ['A','C','C','D'],
]

pattern = [list(input()) for _ in range(2)]
dy = [0, 1, 1]
dx = [1, 0, 1]
cnt = 0
for i in range(2):
    for j in range(3):
        if Map[i][j] == pattern[0][0]:
            flag = 1
            for k in range(3):
                ny, nx = i+dy[k], j+dx[k]
                if Map[ny][nx] == pattern[dy[k]][dx[k]]:
                    pass
                else:
                    flag = 0
            if flag:
                cnt += 1
if cnt:
    print(f'발견({cnt}개)')
else:
    print('미발견')