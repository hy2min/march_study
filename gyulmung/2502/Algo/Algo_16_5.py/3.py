lst = list(map(int, input().split()))
arr = [[0]*3 for _ in range(2)]

count = 0
for i in range(2):
    for j in range(3):
        arr[i][j] = lst[count]
        count += 1

def Max_num(arr):
    Max_n = -1e8
    Max_y, Max_x = 0, 0
    for i in range(2):
        for j in range(3):
            if arr[i][j] > Max_n:
                Max_n = arr[i][j]
                Max_y, Max_x = i, j
    print(f'{Max_y},{Max_x}')

def Min_num(arr):
    Min_n = 1e8
    Min_y, Min_x = 0, 0
    for i in range(2):
        for j in range(3):
            if arr[i][j] < Min_n:
                Min_n = arr[i][j]
                Min_y, Min_x = i, j
    print(f'{Min_y},{Min_x}')

Max_num(arr)
Min_num(arr)