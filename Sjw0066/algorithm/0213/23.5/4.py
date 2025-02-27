arr=[
    [3,5,4,1],
    [1,1,2,3],
    [6,7,1,2],
]

lst=list(map(int,input().split()))
def change(y,x):

    for i in range(4):
        if lst[i] == arr[y][x]:
            if i==3:
                arr[y][x] = lst[0]
                return
            else:
                arr[y][x] = lst[i+1]
                return

for i in range(3):
    for j in range(4):
        change(i,j)

for i in arr:
    for j in i:
        print(j,end=" ")
    print()
