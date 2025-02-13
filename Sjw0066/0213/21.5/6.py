arr=[
    [1,5,3],
    [4,5,5],
    [3,3,5],
    [4,6,2],
     ]

a,b=map(int,input().split())

def change_arr(y,x):

    for i in range(a,b+1):
        if arr[y][x] == i :
            arr[y][x] = 0


for i in range(4):
    for j in range(3):
        change_arr(i,j)

for i in arr:
    for j in i:
        if j == 0:
            print('#',end=" ")
        else:
            print(j,end=" ")
    print()