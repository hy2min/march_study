N,L=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
cnt=1
i=0
j=1
while j<N:

    now=arr[i]
    next=arr[j]

    if next<now+L:
        j+=1
    else:
        i=j
        cnt+=1

    if i >= N - 1: break

print(cnt)
