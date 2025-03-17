T= int(input())
def merge(arr1, arr2):
    global cnt
    temp = []
    index1 = index2 = 0
    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] <= arr2[index2]:
            temp.append(arr1[index1])
            index1 += 1
        else:
            temp.append(arr2[index2])
            index2 += 1

    if index1 == len(arr1):
        temp += arr2[index2:]
    else:
        temp += arr1[index1:]
        cnt += 1
    return temp

def merge_sort(lst1):
    if len(lst1)==1:
        return lst1

    mid=len(lst1)//2
    left=lst1[:mid]
    left=merge_sort(left)
    right=lst1[mid:]
    right=merge_sort(right)
    return merge(left,right)


for tc in range(1,T+1):
    N=int(input())
    lst=list(map(int,input().split()))
    cnt=0
    result=merge_sort(lst)
    print(f'#{tc} {result[len(result)//2]} {cnt}')
