cardlist = list(input())
alp_cnt = [0] * 25
for card in cardlist:
    alp_cnt[ord(card)-65] += 1
cnt = 0
for i in alp_cnt:
    if i > 0:
        cnt += 1
print(f'{cnt}개')
