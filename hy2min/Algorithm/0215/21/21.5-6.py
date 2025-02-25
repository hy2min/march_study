arr = [
    [1,5,3],
    [4,5,5],
    [3,3,5],
    [4,6,2],
]

a, b = map(int, input().split())
for i in range(4):
    for j in range(3):
        if a <= arr[i][j] <= b:
            arr[i][j] = 0


for i in arr:
    for j in i:
        print(j if j != 0 else '#', end=" ")
    print()