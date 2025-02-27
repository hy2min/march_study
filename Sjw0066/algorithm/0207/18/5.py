card_list=list(input())

dat=[0]*100

for i in card_list:
    dat[ord(i)] += 1


print(chr(dat.index(max(dat))))

