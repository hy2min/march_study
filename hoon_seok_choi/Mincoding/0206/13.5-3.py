
arr = []

for i in range(3) :
    arr2 = list(map(int,input().split()))
    arr.append(arr2)


arr3 = []


for i in range(5) :
        a=0
        sum1 = arr[a][i] * arr[a+1][i] + arr[a+2][i]
        a+=1
        arr3.append(sum1)
        a=0


for i in arr3 :
    print(i, end=" ")