import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test in range(1, T+1):
    arr = [list(map(str, input())) for _ in range(5)]
    ret = [[0]*15 for _ in range(5)]
    R_ret = []
    cnt = 0
    while True:
        if cnt == 5:
            break
        for i in range(15):
            if i >= len(arr[cnt]):continue
            ret[cnt][i]=arr[cnt][i]
        cnt += 1

    for i in range(15):
        for j in range(5):
            if ret[j][i] == 0:
                continue
            R_ret.append(ret[j][i])
    print(f'#{test} ', *R_ret, sep ='')