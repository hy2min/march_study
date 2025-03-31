n=int(input())
lst=list(map(int,input().split()))
Min=21e8
Sum=0
for i in range(4):
    Sum+=lst[i]
st=0
ed=4

while 1:
    if ed==n:
        break
    Sum+=lst[ed]
    ed+=1
    Sum-=lst[st]
    st+=1

    if Sum<Min:
        Min=Sum

print(Min)