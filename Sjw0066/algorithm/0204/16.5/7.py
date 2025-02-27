arr=[[0]*4 for _ in range(7)]

num=1
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = num
        num+=1

a,b,c = map(int,input().split())

arr[a] = [0,0,0,0]
arr[b] = [0,0,0,0]
arr[c] = [0,0,0,0]

for i in arr:
    for j in i :
        print(j,end=" ")
    print()