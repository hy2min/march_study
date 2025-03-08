arr = [
    [3,5,9],
    [4,2,1],
    [1,1,5],
]
arr2 = [list(map(int, input().split())) for _ in range(3)]
Sum = 0
for i in range(3):
    for j in range(3):
        if arr2[i][j]:
            Sum += arr[i][j]
print(Sum)