T=int(input())

for tc in range(1,T+1):
    N,*lst=map(int,input().split())
    cnt=0
    Next=0
    flag=0

    while 1:
        cango = Next+lst[Next] + 1
        Max=-21e8
        for i in range(Next,cango):
            nextgo=lst[i] + i + 1
            if  nextgo>=N:
                Next=N
                cnt+=1
                break
            else:
                if nextgo>Max:
                    Max=nextgo
                    Next=i
        if Next==N:break
        cnt+=1


    print(f'#{tc} {cnt}')
