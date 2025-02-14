Map = [['A', 'B', 'G', 'K'], ['T', 'T', 'A', 'B'], ['A', 'C', 'C', 'D']]

Pattern = [list(map(str, input())) for _ in range(2)]

def find_Pattern(y, x):
    cnt = 0
    direct_Y = [1, 0, 1]
    direct_X = [0, 1, 1]
    for i in range(3):
        dy = direct_Y[i] + y
        dx = direct_X[i] + x
        if dy < 0 or dx < 0 or dy >= 3 or dx >= 4:
            break
        elif Map[dy][dx] == Pattern[direct_Y[i]][direct_X[i]]:
            cnt += 1
    return cnt // 3

count = 0
for i in range(3):
    for j in range(4):
        if Map[i][j] == Pattern[0][0]:
            count += find_Pattern(i, j)

if count > 0:
    print(f'발견({count}개)')
else:
    print('미발견')