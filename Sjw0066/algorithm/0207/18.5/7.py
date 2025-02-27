vect="MINCODING"
vect_lst=list(vect)
n=int(input())
target=list(map(str,input().split()))

dat=[0]*100

for i in vect_lst:
    dat[ord(i)] += 1

for i in target:
    if dat[ord(i)] :
        print('O',end="")
    else:
        print('X',end="")
