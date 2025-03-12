arr = [
    ['A','B','C','E','F','G'],
    ['H','I','J','K','L','M'],
    ['N','O','P','Q','R','S'],
]

arr_t = [lst[:] for lst in arr]

def delta(y, x):

    d_y = [-1,1,0,0,0]
    d_x = [0,0,0,-1,1]

    for i in range(5):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if dy < 0 or dx < 0 or dy >= 3 or dx >= 6:
            continue
        if arr[dy][dx] == '#':
            arr[dy][dx] = arr_t[dy][dx]
        else:
            arr[dy][dx] = '#'


lst = list(input())

for char in lst:
    for i in range(3):
        for j in range(6):

            if arr[i][j] == char:
                delta(i, j)
                break
for i in arr:
    for j in i:
        print(j, end="")
    print()