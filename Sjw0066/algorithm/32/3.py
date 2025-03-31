N=int(input())
lst=list(map(int,input().split()))
answer=[]
i=0
while i<len(lst)-2:
    j=i+1
    k=i+2
    if lst[i]==lst[j] and lst[j]==lst[k]:
        lst.pop(i)
        lst.pop(i)
        lst.pop(i)
    else:
        i+=1

lst.sort()
print(*lst)