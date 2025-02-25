arr = [3,5,4,2]
masking = list(map(int, input().split()))
Sum = 0
for i in range(4):
    if masking[i]:
        Sum += arr[i]

print(Sum)