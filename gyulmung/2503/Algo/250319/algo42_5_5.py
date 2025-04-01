import sys
sys.stdin = open('input.txt','r')


import copy
arr = list(map(int, input().split()))
n = int(input())


def Hanhwa(lev, cnt, lst, Sum):
    global Max, arr
    if lev == n:
        if Max < Sum:
            Max = Sum
        return

    # 1번 독수리
    if cnt == 0:
        lst = copy.deepcopy(arr)
        Flag = True
        for i in range(0, 3):
            if arr[i] != 0:
                Flag = False
                break
        if Flag:
            Hanhwa(lev, cnt + 1, lst, Sum)
            arr = lst
        else:
            for i in range(0, 3):
                if arr[i] != 0:
                    Sum += arr[i]
                    arr[i] = 0
                    Hanhwa(lev, cnt + 1, lst, Sum)
                    # 숫자가 없을 때 그냥 넘어가는 것 추가하기
                    arr = lst
                    Sum -= arr[i]


    # 2번 독수리
    if cnt == 1:
        lst = copy.deepcopy(arr)
        Flag = True
        for i in range(3, 6):
            if arr[i] != 0:
                Flag = False
                break
        if Flag:
            Hanhwa(lev, cnt + 1, lst, Sum)
            arr = lst
        else:
            for i in range(3, 6):
                if arr[i] != 0:
                    Sum += arr[i]
                    arr[i] = 0
                    Hanhwa(lev, cnt + 1, lst, Sum)
                    # 숫자가 없을 때 그냥 넘어가는 것 추가하기
                    arr = lst
                    Sum -= arr[i]

    # 3번 독수리
    if cnt == 2:
        lst = copy.deepcopy(arr)
        Flag = True
        for i in range(1, 5):
            if arr[i] != 0:
                Flag = False
                break
        if Flag:
            cnt = 0
            for j in range(len(arr)):
                arr[j] *= 2
            Hanhwa(lev + 1, cnt, lst, Sum)
            arr = lst

        else:
            for i in range(1, 5):
                if arr[i] != 0:
                    Sum += arr[i]
                    arr[i] = 0
                    cnt = 0
                    for j in range(len(arr)):
                        arr[j] *= 2
                    Hanhwa(lev + 1, cnt, lst, Sum)
                    # 숫자가 없을 때 그냥 넘어가는 것 추가하기
                    arr = lst
                    Sum -= arr[i]

lst = []
Max = -1e8
Hanhwa(0, 0, lst, 0)
print(Max)
