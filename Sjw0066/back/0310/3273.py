n=int(input())
lst=list(map(int,input().split()))
x=int(input())

right=n-1
left=0
cnt=0
lst.sort()

while left<right:
    Sum=lst[left]+lst[right]

    if Sum==x:
        left+=1
        right-=1
        cnt+=1
    elif Sum>x:
        right-=1
    elif Sum<x:
        left+=1


print(cnt)