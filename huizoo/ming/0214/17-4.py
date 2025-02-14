arr = [
    ['A','T','K','B'],
    ['C','Z','F','D'],
    ['H','G','E','I'],
]
a, y, x = input().split()
y, x = int(y), int(x)

for i in range(3):
    for j in range(4):
        if arr[i][j] == a:
            print(arr[i+y][j+x])