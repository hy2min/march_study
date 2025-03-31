int1=int(input())

arr=[[0]*4 for _ in range(4)]


for i in range(4):
    for j in range(4):
        arr[i][j] = int1
        int1 += 1
        print(arr[i][j],end=" ")
    print()