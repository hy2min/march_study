T= int(input())


for tc in range(1,T+1):
    N=int(input())
    cards=list(map(str,input().split()))

    sort_cards=[0]*N

    index=0
    for i in range(N):
        sort_cards[index]=cards[i]
        index+=2
        if index>=N:
            index=1

    print(f'#{tc}',end=" ")
    print(*sort_cards)