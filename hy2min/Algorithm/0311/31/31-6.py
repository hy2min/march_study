arr = [1,2,3,3,5,1,0,1,3]
n = int(input())

Min = Sum = sum(arr[:n])
for i in range(len(arr)-n):
    Sum = Sum + arr[n+i] - arr[i]
    Min = min(Sum, Min)
print(Min)