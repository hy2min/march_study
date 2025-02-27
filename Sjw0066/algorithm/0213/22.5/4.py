a,b=map(int,input().split())
arr=[[[0]*3 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(2):
        for k in range(3):
            if j%2==0:
                arr[i][j][k] = a
            else:
                arr[i][j][k] = b

for i in range(3):
    for j in range(2):
        for k in range(3):
            print(arr[i][j][k],end=" ")
        print()
    print()

