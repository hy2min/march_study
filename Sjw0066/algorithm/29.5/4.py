lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))

result=[]
i = 0
j = 0
while i<4 and j<4:
    if lst1[i] <= lst2[j]:
        result.append(lst1[i])
        i+=1
    else:
        result.append(lst2[j])
        j+=1

while i<4:
    result.append(lst1[i])
    i+=1
while j<4:
    result.append(lst2[j])
    j+=1

print(*result)