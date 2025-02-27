index0, index1 = map(int, input().split())
arr = [0]*6
arr[0] = index0
arr[1] = index1

for i in range(0, 4):
    arr[i + 2] = arr[i] * arr[i+1]

print(*arr)