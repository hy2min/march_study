arr = [[3, 1, 9], [7, 2, 1], [1, 0, 8]]

lst = [list(map(int, input().split())) for _ in range(3)]


target = False
for i in range(3):
    for j in range(3):
        if lst[i][j] == 1:
            if 3 <= arr[i][j] <=5:
                target = True

if target:
    print('발견')
else:
    print('미발견')