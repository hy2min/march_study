arr = list(input())
dat = [0]*26
for i in range(8):
    dat[ord(arr[i])-65] += 1
print(chr(dat.index(max(dat))+65))