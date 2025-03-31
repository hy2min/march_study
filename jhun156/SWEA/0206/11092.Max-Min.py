# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [i for i in map(int,input().split())]
    Max_index, Min_index = 0,0
    Max,Min = 21e-8,21e8
    for i in range(N):
        answer = 0
        if Max <= arr[i]:
            Max = arr[i]
            Max_index = i + 1
        if Min > arr[i]:
            Min = arr[i]
            Min_index = i + 1
    answer = Max_index - Min_index
    if answer < 0:
        answer = -answer
    print(f"#{test_case} {answer}")
