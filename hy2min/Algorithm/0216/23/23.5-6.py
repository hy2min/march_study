arr1 = [list(input()) for _ in range(4)]
arr2 = [
    ['A','B','C','D'],
    ['B','B','A','B'],
    ['C','B','A','C'],
    ['B','A','A','A'],
]

cnt = [0] * 4
for i in range(4):
    for j in range(4):
        if arr1[i][j] == arr2[i][j] == 'A':
            cnt[0] += 1
        elif arr1[i][j] == arr2[i][j] == 'B':
            cnt[1] += 1
        elif arr1[i][j] == arr2[i][j] == 'C':
            cnt[2] += 1
        elif arr1[i][j] == arr2[i][j] == 'D':
            cnt[3] += 1
ans = cnt.index(max(cnt))
print(chr(ans+65))