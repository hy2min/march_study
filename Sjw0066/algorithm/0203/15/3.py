lst1=list(map(int,input().split()))

flag=0

for i in range(len(lst1)):
    if i == 0:
        continue
    if abs(lst1[i] - lst1[i-1]) > 3 :
        flag=1

if flag==1:
    print('재배치필요')
else: 
    print('완벽한배치')