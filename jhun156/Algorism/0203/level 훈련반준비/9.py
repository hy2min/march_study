# 민코딩 훈련반 준비 9번
arr = []
row = list(map(int,input().split()))
if len(row) == 3:
    arr.append(row)
    row = list(map(int,input().split()))
    arr.append(row)
    lst = []
    for i in arr:
        for j in i:
            lst.append(j)
    lst.sort()
    count = 0
    for i in range(2):
        for j in range(3):
            arr[i][j] = lst[count]
            count += 1
    for i in arr:
        for j in i:
            print(j,end=' ')
        print()
elif len(row) == 6:
    arr = row
    arr.sort()
    lst2 = [[0] * 3 for _ in range(2)]
    count = 0
    for i in range(2):
        for j in range(3):
            lst2[i][j] = arr[count]
            count += 1  
    for i in lst2:
        for j in i:
            print(j, end = ' ')
        print()