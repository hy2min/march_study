arr = [0]*6

arr[0],arr[1] = map(int,input().split())

for i in range(4) :
    arr[i+2] = arr[i] * arr[i+1]


print(arr[-1])