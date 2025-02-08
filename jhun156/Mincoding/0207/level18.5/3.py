string = list(input())

DAT = [0] * 27

for i in range(len(string)):
    DAT[ord(string[i])-65] += 1

Max = max(DAT)

for i in range(27):
    if DAT[i] == Max:
        print(chr(i+65))
