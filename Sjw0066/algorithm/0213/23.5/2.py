lst=[list(map(int,input().split())) for _ in range(3)]

flag=0
for i in range(3):
    for j in range(i+1,3):
        if lst[i][0] == lst[j][0] :
            flag=1
        if lst[i][1] == lst[j][1] :
            flag=1

if flag:
    print('위험')
else:
    print('안전')


