arr = list(input())

dat = [0] * 11

for i in arr:
    if 'A' <= i <= 'K':
        i = ord(i) - 65
        dat[i] += 1

max_s = dat.index(max(dat))
min_s = dat.index(min(dat))

print(chr(max_s+65))
print(chr(min_s+65))