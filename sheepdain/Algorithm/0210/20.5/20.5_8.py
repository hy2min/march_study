arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
ret=[]
idx1,idx2=0,0
while idx1<4 and idx2<4:
    if arr1[idx1]<=arr2[idx2]:
        ret.append(arr1[idx1])
        idx1+=1
    else:
        ret.append(arr2[idx2])
        idx2+=1

ret.extend(arr1[idx1:])
ret.extend(arr2[idx2:])
print(*ret)