lst=[list(map(int,input().split())) for _ in range(3)]

for i in lst:
    i.sort()

for i in range(3):
    if lst[i][0] == lst[i][1] and lst[i][0] == lst[i][2]:
        print(lst[i][0])
    else:
        print('x')

