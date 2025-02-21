# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    Sum = 0
    while arr:
        Max = max(arr)
        index = arr.index(Max)
        if index == 0:
            arr.pop(0)
        else:
            for i in range(index):
                Sum += (Max - arr[i])
            del arr[:index+1]

    print(f"#{tc} {Sum}")