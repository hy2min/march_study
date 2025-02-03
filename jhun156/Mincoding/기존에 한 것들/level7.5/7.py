arr = [i for i in map(int,input().split())]
arr2 = []
num = 0

for i in range(3):
    row = []
    for j in range(2):
        row.append(arr[num]+2)
        num += 1
    arr2.append(row)

for i in arr2:
    print(*i)