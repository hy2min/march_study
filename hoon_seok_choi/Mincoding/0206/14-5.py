arr = []

for i in range(3) :
    arr2 = list(map(int,input().split()))
    arr.append(arr2)


sum = 0
for i in range(3) :
    for j in range(i+1) :
        sum += arr[i][j] 


print(sum)

