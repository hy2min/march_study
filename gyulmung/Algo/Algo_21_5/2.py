# import sys
# sys.stdin = open('input.txt', 'r')

arr = [[3, 4, 1, 5], [3, 4, 1, 3], [5, 2, 3, 6]]
Sum = []


for i in range(4):
    arr_sum = 0
    for j in range(3):
        arr_sum += arr[j][i]
    Sum.append(arr_sum)

num = int(input())
print(Sum[num])