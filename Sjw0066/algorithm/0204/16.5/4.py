a,b=map(int,input().split())


arr=[0]*6

arr[0] = a
arr[1] = b

for i in range(2,6):
    arr[i]=arr[i-1]*arr[i-2]


print(arr.pop())