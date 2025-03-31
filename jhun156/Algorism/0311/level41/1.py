arr = [0] * 40
arr[1] = 1

for i in range(2,36):
    arr[i] = arr[i-1] + arr[i-2]

n = int(input())
print(arr[n-1])