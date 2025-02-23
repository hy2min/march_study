arr = [
    [4, 5, 4, 5, 4],
    [8, 9, 8, 9, 8],
    [1, 2, 1, 2, 1],
    [4, 5, 4, 5, 4],
    [6, 7, 6, 7, 6]
]

# a, b = map(int,input().split())

def magic() :
    a, b = map(int,input().split())
    arr[a][b] = arr[a][b] + 1
    if arr[a][b] >= 10 :
        arr[a][b] = 0


magic()
magic()
magic()
magic()
magic()

for i in range(5) : 
    for j in range(5) :
        print(arr[i][j], end="")
    print()
