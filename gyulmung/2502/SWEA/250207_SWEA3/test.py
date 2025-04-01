import sys
sys.stdin = open('input.txt','r')

testcase = int(input())

def Fill_color(y, x):
    cnt = 0
    for i in range(ai[y][1], ai[y][3]+1):
        for j in range(ai[y][0], ai[y][2]+1):
            if i in range(ai[x][1], ai[x][3]+1) and j in range(ai[x][0], ai[x][2]+1):
                cnt += 1
    return cnt


for i in range(1, testcase + 1):
    N = int(input())
    ai = [list(map(int, input().split())) for _ in range(N)]
    Fill_box = 0
    result = 0
    for j in range(N-1):
        for k in range(j + 1, N):
            if ai[j][-1] == ai[k][-1]:
                continue
            else:
                Fill_box = Fill_color(j, k)
                result += Fill_box
    print(f'#{i} {result}')
