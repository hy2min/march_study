arr = [
    ['A','T','K','B'],
    ['C','Z','F','D'],
    ['H','G','E','I'],
]

a,b,c = input().split()
b,c = int(b), int(c)

for i in range(3):
    for j in range(4):
        if arr[i][j] == a:
            print(arr[i+b][j+c])
