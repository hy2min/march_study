T= int(input())

for tc in range(1, T + 1):
    N=int(input())
    arr=list(map(int,input().split()))
    dat=[0]*101
    sorted_lst=[0]*N
    answer=[0]*N
    # dat통해 값 정렬
    for i in arr:
        dat[i] += 1

    for i in range(1,len(dat)):
        dat[i] = dat[i] + dat[i-1]

    for i in range(1,len(dat)):
        if i in arr:
            sorted_lst[dat[i]-1]=i

    # 정렬된 값으로 다시 답 배열 만들기
    index_help=-1
    for i in range(len(sorted_lst)):
        if i%2==0:
            answer[i] = sorted_lst[N-i+index_help]
            index_help+=1
        else:
            answer[i] = sorted_lst[i//2]

    print(f'#{tc}',end=' ')
    for i in range(10):
        print(answer[i],end=" ")
    print()