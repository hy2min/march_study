T=int(input())

for tc in range(1,T+1):
    N=int(input())

    lst=list(map(int,input().split()))

    Max=lst[-1] # 최댓값 제일 끝 인덱스로 설정
    price=0
    for i in range(N-1,-1,-1):
        if lst[i] > Max :
            Max = lst[i] # 가격이 더 비싸면 구매 x
        else:
           price+=Max-lst[i] #가격이 최대인 날에 판다고 치고 구매

    print(f'#{tc} {price}')