a,b = map(int,input().split())
arr = [[[0] * 3 for _ in range(2)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        arr[i][0][j] = a
        arr[i][1][j] = b

for i in range(3):
    for j in range(2):
        for k in range(3):
            print(arr[i][j][k],end=' ')
        print()
    print()