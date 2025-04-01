import sys
sys.stdin =open('input.txt','r')

T = 1
for test in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    lst = [0]*(N+1)
    for i in range(1, N+1):
        lst[i] = arr[i][1]
    print(arr)
    print(lst)