arr=[list(map(int,input().split()))+[0] for _ in range(3)]
arr.append([0,0,0,0])


row=0
col=0
cross=0
for i in range(3):
    col=0
    row=0
    for j in range(3):
        row += arr[i][j]
        col += arr[j][i]
    cross += arr[i][i]

    arr[i][3]=row
    arr[3][i]=col
    arr[3][3]=cross

for i in arr:
    for j in i:
        print(j,end=" ")
    print()