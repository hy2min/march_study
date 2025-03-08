arr = [[0]*4 for _ in range(4)]
for i in range(3):
    inputs = list(map(int, input().split()))
    for j in range(3):
        arr[i][j] = inputs[j]

for i in range(3):
    arr[i][3] = sum(arr[i])

for j in range(3):
    for i in range(3):
        arr[3][j] += arr[i][j]

for k in range(3):
    arr[3][3] += arr[k][k]

print('\n'.join(' '.join(map(str, row)) for row in arr))
