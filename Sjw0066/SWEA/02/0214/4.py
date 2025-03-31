T=10
for tc in range(1,T+1):

    N,M = map(str,input().split())

    lst=list(map(int,M))

    i=0
    while 1:
        if i == len(lst)-1 :
            break

        if lst[i] == lst[i+1]:
            lst.pop(i)
            lst.pop(i)
            if i>0:
                i=0
        else:
            i+=1

    print(f'#{tc}',end=" ")
    for i in range(len(lst)):
        print(lst[i],end="")
    print()


