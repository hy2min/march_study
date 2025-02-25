colored_arr = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1],
]

arr = [
    [3, 5, 4, 1, 1],
    [3, 5, 2, 5, 6],
]

check_arr = []

n = int(input())

for i in range(2):
    for j in range(5):
        if colored_arr[i][j] == 1:
            check_arr.append(arr[i][j])

if n in check_arr:
    print(f'{n} 존재')
else:
    print(f'{n} 없음')