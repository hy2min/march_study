arr = input()

dat = [0] * 26

for alp in arr : 
    dat[ord(alp)-65] += 1

most_alp = chr(dat.index(max(dat))+65)

print(most_alp)