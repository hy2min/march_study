arr = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1],
]
arr2 = [
    [3, 5, 4, 1, 1],
    [3, 5, 2, 5, 6],
]
n = int(input())
flag = 0
for i in range(2):
    for j in range(5):
        if arr[i][j] and arr2[i][j] == n:
            flag = 1

if flag:
    print(f'{n} 존재')
else:
    print(f'{n} 없음')

arr.sort()
arr2 = sorted(arr)
