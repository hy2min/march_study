st = input()
dat = [0]*100
for s in st:
    dat[ord(s)] += 1

for i in range(100):
    if dat[i]:
        print(f'{chr(i)}:{dat[i]}')