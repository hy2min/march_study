arr=[]


for i in range(3,0,-1) :
    arr.append([4*i,4*i-1,4*i-2,4*i-3])

int1=int(input())

for i in range(4):
    arr[int1-1][i] = 7

for i in range(3):
    for j in range(4):
        print(arr[i][j],end=" ")
    print()