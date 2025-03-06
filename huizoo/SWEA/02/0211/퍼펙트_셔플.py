T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(input().split())
    new_card = []
    if N % 2 == 0:
        left_card = card[:N//2]
        right_card = card[N//2:]
    else:
        left_card = card[:N//2+1]
        right_card = card[N//2+1:]
    for i in range(N//2):
        new_card.append(left_card[i])
        new_card.append(right_card[i])
    if N % 2 == 1:
        new_card.append(left_card[-1])

    print(f'#{tc}', *new_card)


