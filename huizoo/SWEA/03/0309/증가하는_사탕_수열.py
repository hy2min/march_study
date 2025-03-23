
t = int(input())
def abc(a, b, c):
    if b < c:
        if a < b:
            return 0
        else:
            cnt = a - (b - 1)
            if a - cnt == 0:
                return -1
            else:
                return cnt
    else:
        cnt1 = b - (c - 1)
        if b - cnt1 == 0:
            return -1
        else:
            b = c - 1
            if a < b:
                return cnt1
            else:
                cnt2 = a - (b - 1)
                if a - cnt2 == 0:
                    return -1
                else:
                    return cnt1+cnt2

for tc in range(1, t+1):
    A, B, C = map(int, input().split())
    print(f'#{tc} {abc(A, B, C)}')
