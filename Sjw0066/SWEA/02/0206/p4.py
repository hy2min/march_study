T = int(input())

for tc in range(1, T + 1):
    N=int(input())
    int_a=list(map(int,input()))

    max_cnt=0
    idx=0
    for i in range(N):
        if int_a[i] == 0 :
            continue
        else:
            cnt=0
            idx=i
            while idx < N and int_a[idx] == 1:
                cnt+=1
                idx+=1
        if cnt>max_cnt:
            max_cnt=cnt

    print(f'#{tc} {max_cnt}')