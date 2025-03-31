arr=[4,1,7,9,6,3,3,6]

# pivot,a,b
# pivot은 처음에 0번 idx의 값

# 1. a가 pivot 보다 클때까지 이동
# 2. b가 pivot 보다 작거나 같을때까지 이동
# 3. a와 b를 스왑

# 첫 회전
# a=7
# b=3
# 스왑

# arr=[4,1,3,9,6,3,7,6]
'''
반복 하다가
a랑 b랑 엇갈리면
b랑 pivot 스왑하게되면 정렬 완료
'''
# pivot의 위치를 계속 잡아주는 코드임 ㅇㅇ

def quick(lst):

    if len(lst)<=1:
        return lst

    pivot=0
    a=1
    b=len(lst)-1
    temp=lst[:]

    while 1:
        while a<len(temp) and temp[a]<=temp[pivot]:
            a+=1
        while b>0 and temp[b]>temp[pivot]:
            b-=1
        if a>b:break
        temp[a],temp[b] = temp[b],temp[a]

    temp[pivot],temp[b] = temp[b],temp[pivot]

    left=temp[:b]
    right=temp[b+1:]
    left_lst=quick(left)
    right_lst=quick(right)

    ret=[]
    ret+=left_lst
    ret+=[temp[b]]
    ret+=right_lst

    return ret

arr=list(map(int,input().split()))
ret1=quick(arr)
print(ret1)
