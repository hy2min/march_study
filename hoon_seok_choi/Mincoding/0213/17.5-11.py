arr =[3,5,4,2]

arr2 = list(map(int,input().split()))
sum1=0
for i in range(4) :
    if arr2[i] == 1 :
        sum1 += arr[i]

print(sum1)

