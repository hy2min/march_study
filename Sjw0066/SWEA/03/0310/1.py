T=int(input())

for tc in range(1,T+1):
    lst=list(map(int,input().split()))
    cnt=0
    while lst[1]>=lst[2] :
        lst[1] -=1
        cnt+=1
    while lst[0]>=lst[1]:
        lst[0] -= 1
        cnt+=1

    if lst[0] ==0 or lst[1] ==0 or lst[2] ==0 :
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {cnt}')



