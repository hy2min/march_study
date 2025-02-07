arr=list(input())

dat=[0] * 100

for i in arr:
    dat[ord(i)] += 1
    
print(chr(dat.index(max(dat))))
