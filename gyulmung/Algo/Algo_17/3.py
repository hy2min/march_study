arr = [[3, 5, 9], [4, 2, 1], [1, 1, 5]]

lst = [list(map(int, input().split())) for i in range(3)]

Sum_arr = 0

for i in range(3):
    for j in range(3):
        if lst[i][j] == 1:
            Sum_arr += arr[i][j]

print(Sum_arr)