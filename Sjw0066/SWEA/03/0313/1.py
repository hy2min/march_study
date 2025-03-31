T=int(input())

for tc in range(1,T+1):
    N,M=map(int,input().split())
    con=list(map(int,input().split()))
    truck=list(map(int,input().split()))
    answer=0
    con.sort(reverse=True)
    truck.sort(reverse=True)

    for i in range(M):
        now=truck[i]
        Max=-21e8
        Max_idx=0
        flag=0
        for j in range(len(con)):
            if con[j]<=now:
                if con[j]>Max:
                    Max=con[j]
                    Max_idx=j
                    flag=1
        if flag:
            answer+=Max
            con.pop(Max_idx)


    print(f'#{tc} {answer}')