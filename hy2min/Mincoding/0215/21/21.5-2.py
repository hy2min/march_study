arr = [
    [3,4,1,5],
    [3,4,1,3],
    [5,2,3,6],
]
sum_arr = [0] * 4

for i in range(3):
    for j in range(4):
        sum_arr[j] += arr[i][j]

n = int(input())
print(sum_arr[n])