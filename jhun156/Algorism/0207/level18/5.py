abc = list(input())

DAT = [0] * 27

for i in range(len(abc)):
    DAT[ord(abc[i])-65] += 1
tmp = max(DAT)
for i in range(27):
    if DAT[i] == tmp:
        print(chr(i+65))