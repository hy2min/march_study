lst=list(input())
a,b=map(str,input().split())
ai=0
bi=0
for i in range(len(lst)):
    if lst[i] == a:
        ai=i
    if lst[i] == b:
        bi=i

for i in range(-1,2,2):
    ani = ai+i
    bni = bi+i
    if ani>=0 and ani<len(lst):
        lst[ani] = '#'
    if bni >= 0 and bni < len(lst):
        lst[bni] = '#'

for i in lst:
    print(i,end="")
