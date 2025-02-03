arr = [
    [3,5,14],
    [2,3,9],
    [6,2,7],
]

a = int(input())
count = 0

for i in range(3):
    for j in range(3):
        if arr[i][j] % a == 0:
            count += 1

print(count)