arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr= arr1+arr2
def merge(start,end):
    global arr,result
    mid=(start+end)//2

    if start==end: return

    merge(start,mid)
    merge(mid+1,end)

    a=start
    b=mid+1
    result=[]

    while 1:
        if a>mid and b>end: break
        if a>mid:
            result.append(arr[b])
            b+=1
        elif b>end:
            result.append(arr[a])
            a+=1
        elif arr[a]<arr[b]:
            result.append(arr[a])
            a+=1
        else:
            result.append(arr[b])
            b+=1

    for i in range(len(result)):
        arr[start+i]=result[i]

merge(0,7)
print(*arr)