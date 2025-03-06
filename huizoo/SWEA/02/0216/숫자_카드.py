t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = input()
    dat = [0]*10
    for i in range(N):
        dat[int(arr[i])] += 1
    Max = max(dat)
    if dat.count(Max) != 1:
        print(f'#{tc} {9 - dat[::-1].index(Max)} {Max}')
    else:
        print(f'#{tc} {dat.index(Max)} {Max}')