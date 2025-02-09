dat=[0] * 100

for i in range(3):
    str_lst=list(input())
    for j in str_lst:
        dat[ord(j)] += 1

if max(dat)==1 :
    print('Perfect')
else:
    print('No')