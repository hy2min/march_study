import sys
sys.stdin = open('input.txt','r')

def rotation(lev, lst):
    global Max
    if lev == rotate:
        ret = int("".join(lst))
        Max = max(Max,ret)
        return

    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            lst[i], lst[j] = lst[j], lst[i]
            rotation(lev+1, lst)
            lst[i], lst[j] = lst[j], lst[i]

T = int(input())
for test in range(1, T+1):
    input_num = input().split()
    arr, rotate = input_num
    arr = list(arr)
    rotate = int(rotate)
    visited = set()
    Max = -1e8

    if rotate <= 5:
        rotation(0, arr)
    else:
        for i in range(len(arr) // 2):
            k = arr.index(max(arr[i:]))
            arr[i], arr[k] = arr[k], arr[i]
        if (rotate - (len(arr) // 2)) % 2 !=0:
            rotate = 1
            rotation(0, arr)
        else:
            rotate = 2
            rotation(0, arr)

    print(f'#{test} {Max}')
