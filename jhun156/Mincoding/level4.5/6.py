arr = [3,9,12,15,55]

a,b,c = map(int,input().split())

sum = a + b + c

if sum > 10:
    print(arr[4])
else:
    print(arr[0])