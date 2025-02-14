lst = [['_']*5 for _ in range(4)]

Y, X = map(int, input().split())
Y1, X1 = map(int, input().split())
def bomb(y, x):
    global lst
    direct_Y = [0, 0, 1, -1, 1, 1, -1, -1]
    direct_X = [1, -1, 0, 0, 1, -1, 1, -1]
    for i in range(8):
        dy = direct_Y[i] + y
        dx = direct_X[i] + x
        if dx <0 or dy < 0 or dx >= 5 or dy >= 4:
            continue
        lst[dy][dx] = '#'
    return lst


bomb_lst = bomb(Y, X)
bomb_lst = bomb(Y1, X1)
for i in range(4):
    for j in range(5):
        print(lst[i][j], end = ' ')
    print()