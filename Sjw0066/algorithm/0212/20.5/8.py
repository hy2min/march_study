def array_sort(index1,index2):
    if index1>3:
        while index2<=3:
            lst.append(arr2[index2])
            index2+=1
        return

    if index2>3:
        while index1 <= 3:
            lst.append(arr1[index1])
            index1 += 1
        return

    if arr1[index1] <= arr2[index2]:
        lst.append(arr1[index1])
        array_sort(index1 + 1, index2)
    else:
        lst.append(arr2[index2])
        array_sort(index1, index2 + 1)

lst=[]

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
array_sort(0,0)
print(*lst)