arr = [
    [3,5,4,1],
    [1,1,2,3],
    [6,7,1,2],
]

lst = list(map(int,input().split()))
s_lst = []
for i in range(1,4):
    s_lst.append(lst[i])
s_lst.append(lst[0])

for i in range(3):
    for j in range(4):
        for k in range(4):
            if arr[i][j] == lst[k]:
                arr[i][j] = str(s_lst[k])

for i in range(3):
    print(*arr[i])
