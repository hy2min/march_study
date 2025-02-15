st = input()
dat = [0]*100
for i in st:
    dat[ord(i)] += 1
print(chr(dat.index(max(dat))))