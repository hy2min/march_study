arr = [[1, 3, 3, 5, 1], [3, 6, 2, 4, 2], [1, 9, 2, 6, 5]]
lst = [0]*10

num = int(input())

for i in range(3):
    for j in range(5):
        lst[arr[i][j]] += 1

for i in range(1, 10):
    if lst[i] == num:
        print(i, end = " ")