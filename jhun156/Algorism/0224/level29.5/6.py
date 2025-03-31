lst = [
    [3,7,4],
    [2,6,9],
    [5,1,2],
    [3,6,7],
]

arr = list(map(int,input().split()))

for i in range(4):
    cnt = 0
    while cnt < arr[i]:
        tmp = lst[i].pop()
        lst[i].insert(0,tmp)
        cnt += 1

for i in range(3):
    for j in range(4):
        print(lst[j][i],end='')
    print()