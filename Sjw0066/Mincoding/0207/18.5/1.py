arr=[['G','K','G']]
arr.append(list(map(int,input().split())))

dat=[0] * 100

for i in range(2):
    for j in range(3):
        dat[ord(arr[i][j])] += 1

if max(dat) >= 3 :
    print('있음')
else :
    print('없음')


