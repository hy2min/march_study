lst=[1,2,3,3,5,1,0,1,3]
N=int(input())
Min=21e8
Sum=0
for i in range(N):
    Sum+=lst[i]
st=0
ed=N

while ed<len(lst):

    Sum+=lst[ed]
    ed+=1
    Sum-=lst[st]
    st+=1
    if Min>Sum:
        Min=Sum

print(Min)