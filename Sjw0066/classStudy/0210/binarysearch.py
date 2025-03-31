# 이진 탐색
# 숫자 업다운이라고 생각하면 편함 ㅇㅇ
# O log n  속도임 sort 를 하고 하려면 nlogn

arr = [2, 3, 4, 7, 8, 10, 11, 13, 15]


def bs(st,ed,target):
    while 1:
        mid=(st+ed)//2
        if arr[mid] == target:
            return 1

        elif arr[mid] > target:
            ed=mid-1

        elif arr[mid] < target:
            st=mid+1

        if st>ed:
            return 0


result = bs(0, 8, 12)

print(result)

