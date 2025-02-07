str_lst=list(input())

flag=0
for i in range(len(str_lst)-4):
    if str_lst[i:i+5] == list('GHOST'):
        flag=1
        break

if flag:    
    print('존재')
else:    
    print('없음')