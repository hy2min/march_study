st = input()
dat = [0]*26
for alp in st : 
    dat[ord(alp)-65] += 1
print(chr(dat.index(max(dat))+65))