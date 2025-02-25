L=int(input())
N=int(input())

dat=[0]*L
request_guest=0
request_bread=0
real_guest=0
real_bread=0

for i in range(N):
    cnt=0
    p,k = map(int,input().split())
    
    if k-p+1>request_bread:
        request_guest=i+1
        request_bread=k-p+1

    for j in range(p,k+1):
        if dat[j-1] :
            continue
        else:
            dat[j-1] += 1
            cnt+=1
    
    if cnt>real_bread:
        real_bread=cnt
        real_guest=i+1

print(request_guest)
print(real_guest)
    
