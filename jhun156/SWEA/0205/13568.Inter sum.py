# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int,input().split()))
    lst = list(map(int,input().split()))

    def inter_sum(start_index, num):
        result = 0
        for i in range(start_index,start_index + num):
            result += lst[i]
        return result

    Max, Min = inter_sum(0, arr[1]), inter_sum(0, arr[1])
    for i in range(arr[0]-arr[1]+1):
        if Max < inter_sum(i, arr[1]):
            Max = inter_sum(i, arr[1])
        if Min > inter_sum(i, arr[1]):
            Min = inter_sum(i, arr[1])
    print(f"#{test_case} {Max - Min}")