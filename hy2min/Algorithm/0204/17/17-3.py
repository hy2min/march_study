arr = [
    [3, 5, 9],
    [4, 2, 1],
    [1, 1, 5],
]

colored_arr = []
for _ in range(3):
    colored_arr.append(list(map(int, input().split())))

total = 0
for i in range(3):
    for j in range(3):
        if colored_arr[i][j] == 1:
            total += arr[i][j]

print(total)