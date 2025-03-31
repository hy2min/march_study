import sys
sys.stdin = open('input.txt', 'r')

testcase = int(input())

def Average(N):
    Sum_num = 0
    for i in ai:
        for j in i:
           Sum_num += j
    return Sum_num / N**2


for i in range(1, testcase + 1):
    N, M = map(int, input().split())
    ai = [list(map(int, input().split())) for _ in range(N)]+
    average_fly = Average(N)
    arr = []
    Dead_fly = 0
    for j in range(N-1):
        for k in range(N-1):
            if ai[j][k] <= average_fly:
                continue
            else:
                Dead_fly = ai[j][k] + ai[j + 1][k] + ai[j][k + 1] + ai[j + 1][k + 1]
                arr.append(Dead_fly)
    print(f'#{i} {max(arr)}')