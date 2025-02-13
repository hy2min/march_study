arr = [
    [3, 55, 42],
    [-5, -9, -10]
]


pix = [list(map(int,input().split())) for _ in range(2)]

for i in range(2) :
    for j in range(2) :
        if pix[i][j] in [*arr[0],*arr[1]] :
            print('Y', end= " ")
        else :
            print('N',end= " ")
    print()