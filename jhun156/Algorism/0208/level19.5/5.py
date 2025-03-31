sketchbook = []
for i in range(3):
    row = list(input())
    sketchbook.extend(row)

DAT = [0] * 27

for i in range(len(sketchbook)):
    DAT[ord(sketchbook[i]) - 65] += 1

for i in range(27):
    if DAT[i] != 0:
        print(chr(i+65),end='')