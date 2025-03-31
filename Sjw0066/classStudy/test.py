# im

T=int(input())

for tc in range(1,T+1):
    N=int(input())
    lst=list(map(int,input().split()))
    Max=-21e8

    for i in range(N-1):
        check=lst[i]
        cnt=0
        for j in range(i+1,N):
            if lst[j] > check:
                cnt+=1
                check=lst[j]
        if Max<cnt:
            Max=cnt

    print(f'#{tc} {Max}')
