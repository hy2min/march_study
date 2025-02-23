arr2 = [3,7,4,9]

arr = list(map(int,input().split()))

if arr2 == arr :
    print('pass')
for i in range(4) :
    if arr2[i] != arr[i] :
        print("fail")
        break

