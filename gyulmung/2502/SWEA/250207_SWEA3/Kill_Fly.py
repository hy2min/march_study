import sys
sys.stdin = open('input.txt', 'r')

testcase  = int(input())


def getSum(a, b):
    Sum = 0
    for i in range(M):
        for j in range(M):
            Sum += ai[i + a][j + b]
    return Sum


for i in range(1, testcase + 1):
    N, M = map(int, input().split())
    ai = [list(map(int, input().split())) for _ in range(N)]
    Max = -1e8

    for j in range(N - M + 1):
        for k in range(N - M + 1):
            ret = getSum(j, k)
            if ret > Max:
                Max = ret
    print(f'#{i} {Max}')