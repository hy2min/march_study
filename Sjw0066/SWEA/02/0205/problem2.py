T=int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    v= list(map(int,input().split()))

    max_sum=-1e21
    min_sum=1e21

    for i in range(len(v)-M+1):
        cal_v=v[i:i+M]
        
        sum_cal_v=0

        for j in cal_v:
            sum_cal_v+=j

        if sum_cal_v>max_sum:
            max_sum=sum_cal_v
        if sum_cal_v<min_sum:
            min_sum=sum_cal_v

    answer=max_sum-min_sum
    print(f'#{test_case} {answer}')