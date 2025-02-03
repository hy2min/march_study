arr = [i for i in map(int,input().split())]

lst = []

count = 5

for i in range(2):
    row = []
    for j in range(3):
        row.append(arr[count])
        count -= 1
    lst.append(row)
    
arr2 = []
for i in range(2):
    for j in range(3):
        arr2.append(lst[i][j])

arr2[0],arr2[5] = arr2[5],arr2[0]

print(*arr2)