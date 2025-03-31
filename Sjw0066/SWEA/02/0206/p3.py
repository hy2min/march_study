T = int(input())

for tc in range(1, T + 1):
    N=int(input())
    int_a=list(map(int,input().split()))

    answer=0
    min_val=21e8
    max_val=-21e8
    min_index=0
    max_index=0

    for i in range(N):
        if int_a[i] >= max_val:
            max_val=int_a[i]
            max_index=i
        if int_a[i]< min_val:
            min_val=int_a[i]
            min_index=i

    answer=abs(max_index-min_index)



    print(f'#{tc} {answer}')