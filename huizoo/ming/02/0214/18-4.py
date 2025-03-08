cardlist = list(input())
dat = [0]*26
for card in cardlist:
    dat[ord(card)-65] += 1

cnt = 0
for i in range(26):
    if dat[i]: cnt += 1

print(f'{cnt}개')