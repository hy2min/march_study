lst = ['Amy','Bob','Chloe','Diane','Edger']
arr = [
    [0,0,0,0,1],
    [1,0,0,0,0],
    [0,1,0,0,0],
    [0,1,0,0,0],
    [0,0,0,0,0],
]
tmp = 0
max = 0
index = -1
for i in range(5):
    tmp = 0
    for j in range(5):
        tmp += arr[j][i]
    if tmp > max:
        max = tmp
        index = i

print(lst[index])