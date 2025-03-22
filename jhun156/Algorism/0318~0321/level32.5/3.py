arr = [
    ['A','B','C','E','F','G'],
    ['H','I','J','K','L','M'],
    ['N','O','P','Q','R','S'],
]

for i in range(3):
    for j in range(6):
        arr[i][j] = [0,arr[i][j],'#']

# 0이면 숫자 출력
# 1이면 # 출력

cok = list(input())
diY = [-1,1,0,0,0]
diX = [0,0,-1,1,0]

for i in range(3):
    for j in range(6):
        for alpha in cok:
            if arr[i][j][1] == alpha:
                for w in range(5):
                    dy = i + diY[w]
                    dx = j + diX[w]
                    if dy < 0 or dy > 2 or dx < 0 or dx > 5:
                        continue
                    arr[dy][dx][0] = 1 - arr[dy][dx][0]

for i in range(3):
    for j in range(6):
        if arr[i][j][0] == 0:
            print(arr[i][j][1],end='')
        else:
            print(arr[i][j][2],end='')
    print()