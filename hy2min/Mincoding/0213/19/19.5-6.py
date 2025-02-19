map_arr = [
    ['A','B','G','K'],
    ['T','T','A','B'],
    ['A','C','C','D'],
]

pattern = [list(input()) for _ in range(2)]

def find_pattern(y,x):
    for i in range(2):
        for j in range(2):
            if map_arr[y+i][x+j] != pattern[i][j]:
                return 0
    return 1

cnt = 0
for y in range(2):
    for x in range(3):
        if find_pattern(y,x) == 1:
            cnt += 1

if cnt > 0:
    print(f'발견({cnt}개)')
else:
    print('미발견')