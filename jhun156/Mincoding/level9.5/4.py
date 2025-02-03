arr = [
    [10,3,20],
    [60,30,40],
    [20,30,40],
]

a,b = input().split()
count = 0

for i in range(3):
    for j in range(3):
        if int(a) <= arr[i][j] <= int(b):
            count += 1

print(count)