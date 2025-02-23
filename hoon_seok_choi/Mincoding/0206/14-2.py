
arr = []

for i in range(5) :
    arr2 = list(map(int,input().split()))
    arr.append(arr2)

arr_sum = []

sum =0

for i in range(5) :
    for j in range(4) :
        sum += arr[i][j]
    arr_sum.append(sum)
    sum=0

for i in arr_sum :
    print(i, end=" ")
