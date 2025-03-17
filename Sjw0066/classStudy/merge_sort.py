'''
선택
삽입
버블          n^2
힙
합병
퀵           nlogn
계수정렬        n
'''

# 힙은 안정적으로 nlogn / 구현빡셈

def merge_sort(lst):

    if len(lst)<=1:
        return lst

    mid=len(lst)//2
    left=lst[:mid]
    right=lst[mid:]
    left_lst=merge_sort(left)
    right_lst=merge_sort(right)

    return merge(left_lst,right_lst)

def merge(left,right):
    idx1=0
    idx2=0
    result=[]
    while idx1<len(left) and idx2<len(right):
        if left[idx1]<right[idx2]:
            result.append(left[idx1])
            idx1+=1
        else:
            result.append(right[idx2])
            idx2+=1

    if len(left) == idx1:
        result+=right[idx2:]
    if len(right) == idx2:
        result += left[idx1:]

    return result

arr=[2,7,5,3,1,5,9,2]
ret=merge_sort(arr)
print(ret)