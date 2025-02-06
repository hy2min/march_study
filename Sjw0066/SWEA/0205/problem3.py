
T=int(input())

for test_case in range(1,T+1):
    N=int(input())
    lst1= list(map(int,input().split()))

    lst_max=-1e21
    lst_min=1e21

    for i in lst1:
        if i > lst_max:
            lst_max=i
        if i<lst_min:
            lst_min=i
        
    answer=lst_max-lst_min
    print(f'#{test_case} {answer}')