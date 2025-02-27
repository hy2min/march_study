lst1=list(map(int,input().split()))

cnt=0
lst1.sort()
flag=True

while flag:
    lst1[0]+=1
    cnt+=1

    if lst1[0]==100 :
        break
    

print(cnt)