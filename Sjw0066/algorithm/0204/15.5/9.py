arr=[list(map(int,input().split())) for _ in range(2)]

arr2=[]
for i in arr:
    for j in i:
        arr2.append(j)

arr2.sort()

index=0
for i in range(2):
    for j in range(3):
        arr[i][j] = arr2[index]
        index+=1
        print(arr[i][j],end=" ")
    print()


