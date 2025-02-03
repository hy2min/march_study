arr1 = [2,1,2,4,5]
arr2 = [
    [2,5,3],
    [4,5,7],
    [8,7,2],
]

a = int(input())
count = 0

for i in arr1:
    if i == a:
        count += 1

for i in range(3):
    for j in range(3):
        if arr2[i][j] == a:
            count += 1

print(count)