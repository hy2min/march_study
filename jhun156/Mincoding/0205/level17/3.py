arr = [
    [3,5,9],
    [4,2,1],
    [1,1,5],
]

lst = [[i for i in map(int,input().split())] for _ in range(3)]
sum = 0
for i in range(3):
    for j in range(3):
        if lst[i][j] == 1:
            sum += arr[i][j]
print(sum)