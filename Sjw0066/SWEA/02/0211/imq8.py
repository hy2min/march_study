T= int(input())

for tc in range(1, T + 1):
    N= int(input())

    k=0
    set1=set()

    while 1:
        k+=1
        int1=N*k

        lst1=list(str(int1))

        for i in range(len(lst1)):
            set1.update(lst1[i])
        if len(set1) == 10 :
            break

    answer=k*N
    print(f'#{tc} {answer}')
