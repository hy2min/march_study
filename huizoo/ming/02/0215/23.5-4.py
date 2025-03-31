import copy
arr1 = [
    [3,5,4,1],
    [1,1,2,3],
    [6,7,1,2],
]
arr2 = copy.deepcopy(arr1)
arr3 = list(map(int, input().split()))

for i in range(3):
    for j in range(4):
        for k in range(4):
            if arr1[i][j] == arr3[k]:
                if k == 3:
                    arr2[i][j] = arr3[0]
                else:
                    arr2[i][j] = arr3[k+1]
print('\n'.join(' '.join(map(str, row)) for row in arr2))
