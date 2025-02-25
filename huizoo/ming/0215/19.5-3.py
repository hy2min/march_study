arr = list(map(int, input().split()))
arr2 = [[0]*4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        arr2[i][j] = 4 * i + j + 1
n = 1
for i in range(4):
    for j in range(4):
        flag = 0
        for k in range(4):
            if arr[k] == arr2[i][j]:
                flag = 1
        if flag:
            arr2[i][j] = n
            n += 1
        else:
            arr2[i][j] = 0
print('\n'.join(' '.join(map(str, row)) for row in arr2))




