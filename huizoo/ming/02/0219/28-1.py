name = ['Amy','Bob','Chloe','Diane','Edger']
arr = [
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
like = [0]*len(name)
for j in range(len(name)):
    for i in range(len(name)):
        if arr[i][j] == 1:
            like[j] += 1

print(name[like.index(max(like))])