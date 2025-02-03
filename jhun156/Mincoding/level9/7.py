test = []
for i in range(6):
    a, b =map(int,input().split())
    test.append(a)
    test.append(b)

num = 0
arr = []

for i in range(6):
    row = []
    for j in range(2):
        row.append(test[num])
        num += 1
    arr.append(row)

count = 0

for i in range(6):
    if arr[i][1] > arr[i][0]:
        tmp = arr[i][1]
        arr[i][1] = arr[i][0]
        arr[i][0] = tmp
        count += 1

for i in range(6):
    for j in range(2):
        print(arr[i][j],end=' ')
    print()
print(f"{count}명")
