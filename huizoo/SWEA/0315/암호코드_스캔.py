import sys
sys.stdin = open('input.txt','r')


def abc(st):
    global ans
    if tuple(st) in checked:
        return
    else:
        Sum = 0
        for i in range(8):
            if i % 2 == 0:
                Sum += 3 * st[i]
            else:
                Sum += st[i]
        if Sum % 10 == 0:
            ans += sum(st)
        checked.add(tuple(st))
        return

def bbq(st):
    multi = 2
    copy_st = st[:]
    password = ''.join(map(str, copy_st))
    while password not in PASSWORD:
        for i in range(3):
            copy_st[i] //= multi
        password = ''.join(map(str, copy_st))
        copy_st = st[:]
        multi += 1

    pw2.append(PASSWORD[password])
    return

PASSWORD = {
    '211': 0,
    '221': 1,
    '122': 2,
    '411': 3,
    '132': 4,
    '231': 5,
    '114': 6,
    '312': 7,
    '213': 8,
    '112': 9,
}

T = int(input())
for tc in range(1, T+1):
    if tc == 9:
        debug = 1
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        line = input().strip()
        if line.strip('0'):
            arr.append(line)

    ans = 0
    rows = set()
    checked = set()
    for row in arr:
        if not row: continue
        if row not in rows:
            rows.add(row)
            num = bin(int(row, 16))[2:]
            pw = []
            pw2 = []
            cnt = 0
            flag = 0
            for i in num:
                if flag == 3 and i == '0': continue
                if len(pw2) == 8:
                    abc(pw2)
                    pw2 = []
                if i == '1':
                    if flag == 1:
                        flag += 1
                        pw.append(cnt)
                        cnt = 0
                    if flag == 3:
                        flag = 0
                        bbq(pw)
                        pw = []
                        cnt = 0
                    cnt += 1
                else:
                    if flag == 0:
                        flag += 1
                        pw.append(cnt)
                        cnt = 0
                    if flag == 2:
                        flag += 1
                        pw.append(cnt)
                    cnt += 1
            if flag == 2:
                pw.append(cnt)
            bbq(pw)
            abc(pw2)

    print(f'#{tc} {ans}')
