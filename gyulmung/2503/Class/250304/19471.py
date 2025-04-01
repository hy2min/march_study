import sys
sys.stdin = open('input.txt', 'r')

def Find_x(y,x):
    cnt1, cnt2 = 1, 0
    while True:
        if x - cnt1 < 0 or x + cnt1 >= 100:
            cnt1 = cnt1 * 2 + 1
            break
        if arr[y][x - cnt1] == arr[y][x + cnt1]:
            cnt1 += 1
        else:
            cnt1 = cnt1 * 2 + 1
            break

    while True:
        if x - cnt1 < 0 or x + cnt2 + 1>= 100:
            cnt2 = cnt2 * 2 + 2
            break
        if arr[y][x - cnt2] == arr[y][x + cnt2 + 1]:
            cnt2 += 1
        else:
            cnt2 = cnt2 * 2 + 2
            break
    return max(cnt1, cnt2)

def Find_y(y,x):
    cnt1, cnt2 = 1, 0
    while True:
        if y - cnt1 < 0 or y + cnt1 >= 100:
            cnt1 = cnt1 * 2 + 1
            break
        if arr[y - cnt1][x] == arr[y + cnt1][x]:
            cnt1 += 1
        else:
            cnt1 = cnt1 * 2 + 1
            break

    while True:
        if y - cnt1 < 0 or y + cnt2 + 1>= 100:
            cnt2 = cnt2 * 2 + 2
            break
        if arr[y - cnt2][x] == arr[y + cnt2 + 1][x]:
            cnt2 += 1
        else:
            cnt2 = cnt2 * 2 + 2
            break
    return max(cnt1, cnt2)


T = 10
for test in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(100)]
    print(arr)
    Max = -1e8

    for i in range(100):
        for j in range(100):
            cnt_x = Find_x(i, j)
            cnt_y = Find_y(i, j)
            Max = max(Max, cnt_y, cnt_x)
    print(Max)