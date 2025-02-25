def hash(alp) : 
    return ord(alp)-ord('A')

cardlist = input()
dat = [0] * 26

for card in cardlist : 
    dat[hash(card)] += 1

print(f'{len(dat)-dat.count(0)}개')