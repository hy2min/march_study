lst=list(map(str,input()))
ord_lst=[]
for i in lst:
    ord_lst.append(ord(i))

while 1:
    flag=0

    for i in range(len(ord_lst)):
        if ord_lst[i]>=65:
            print(chr(ord_lst[i]),end="")
            ord_lst[i]-=1
            flag=1
        else:
            print('_',end="")
    print()

    if not flag:
        break


