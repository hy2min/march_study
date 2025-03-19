arr = list(map(int, input().split()))
arr.sort()
Sum = 0
for i in range(4):
    Sum += (3-i)*arr[i]

print(Sum)