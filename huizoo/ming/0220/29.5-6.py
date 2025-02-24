arr = list(map(int, input().split()))
lst = [
    [3,2,5,3],
    [7,6,1,6],
    [4,9,2,7],
]
lst2 = [list(row) for row in zip(*lst)]
for i in range(4):
    for _ in range(arr[i]):
        lst2[i] = [lst2[i][-1]] + lst2[i][:-1]
print('\n'.join(''.join(map(str, row)) for row in list(zip(*lst2))))