N=int(input())
lst=list(map(int,input().split()))
lst.sort()
cnt=0
Sum=0
for i in range(N):
    if Sum<100:
        cnt+=1
        Sum+=lst[i]
        if Sum > 100:
            cnt -= 1
            break
print(cnt)