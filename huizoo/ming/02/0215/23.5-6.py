arr1 = [input() for _ in range(4)]
arr2 = [
    ['A','B','C','D'],
    ['B','B','A','B'],
    ['C','B','A','C'],
    ['B','A','A','A'],
]
dat = [0]*91
for i in range(4):
    for j in range(4):
        if arr1[i][j] == arr2[i][j]:
            dat[ord(arr1[i][j])] += 1

print(chr(dat.index(max(dat))))