lst = [i for i in map(int,input().split())]
arr = []

for i in range(3):
    row = []
    target = lst[i]
    for j in range(4):
        row.append(target)
        target += 1
    arr.append(row)

for i in arr:
    print(*i)