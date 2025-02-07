card_list=list(input())

dat=[0]*100

for i in card_list:
    dat[ord(i)] += 1

while 0 in dat:
    dat.remove(0)

print(f'{len(dat)}개')

