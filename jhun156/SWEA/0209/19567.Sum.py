# import sys
# sys.stdin = open("input.txt","r")

T = 10
for test_case in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    Sum_list = [0] * 202
    for i in range(100):
        for j in range(100):
            Sum_list[i] += arr[i][j]
            Sum_list[i+100] += arr[j][i]
        Sum_list[200] += arr[i][i]
        Sum_list[201] += arr[i][99-i]
    ans = max(Sum_list)

    print(f"#{test_case} {ans}")