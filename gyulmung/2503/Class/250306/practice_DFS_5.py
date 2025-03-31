import sys
sys.stdin = open('input.txt', 'r')
import copy

T = int(input())

for test in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    cnt = 0
    def Queen(y, x):
        global arr
        diry = [0, 0, 1, -1, 1, 1, -1, -1]
        dirx = [1, -1, 0, 0, 1, -1, 1, -1]
        for i in range(8):
            for j in range(N):
                dy = diry[i]*j + y
                dx = dirx[i]*j + x
                if dy < 0 or dx < 0 or dy >= N or dx >= N:
                    continue
                arr[dy][dx] = 1

    def Setting(level):
        global cnt, arr
        Sum = 0
        if level == N:
            cnt += 1
            return
        if level < N:
            for i in arr:
                Sum += sum(i)
            if Sum == N:
                return

        backup = copy.deepcopy(arr)
        for j in range(N):
            if arr[level][j] == 0:
                Queen(level, j)
                Setting(level + 1)
                arr = copy.deepcopy(backup)

    Setting(0)
    print(f'#{test} {cnt}')
