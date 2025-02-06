T = int(input())
for tc in range(1, T+1) : 
    n = int(input())
    card_list = list(map(int, input()))
    dat = [0]*10
    for i in range(n) : 
        dat[card_list[i]] += 1
    max_card = max(dat)
    while dat.count(max_card) != 1 : 
        dat[dat.index(max_card)] = 0
    print(f'#{tc} {dat.index(max_card)} {max_card}')