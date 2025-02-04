flag=0

for i in range(3):
    a=input()
    if 'M' in a :
        flag=1

if flag==1:
    print('M이 존재합니다')
else:
    print('M이 존재하지 않습니다')