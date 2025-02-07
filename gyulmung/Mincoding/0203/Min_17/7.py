arr = [[0, 0, 1, 0, 0], [0, 0, 1, 1, 1]]
lst = [[3, 5, 4, 1, 1], [3, 5, 2, 5, 6]]

num = int(input())

for i in range(2):
    for j in range(5):
        if num == lst[i][j]:
            y, x = i, j

if arr[y][x] == 1:
    print(f'{lst[y][x]} 존재')
else:
    print(f'{lst[y][x]} 없음')