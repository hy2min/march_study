def rotate(arr):
    return [[arr[2-i][j] for i in range(3)] for j in range(3)]

arr = [
    ['_','5','4'],
    ['3','_','_'],
    ['_','_','1'],
]

n = int(input())


for _ in range(n):
    arr = rotate(arr)

for i in arr:
    for j in i:
        print(j,end='')
    print()