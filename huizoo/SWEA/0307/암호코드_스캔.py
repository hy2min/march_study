from collections import deque
import sys

sys.stdin = open("input.txt", "r")

PASSWORD = [
    [3, 2, 1, 1],
    [2, 2, 2, 1],
    [2, 1, 2, 2],
    [1, 4, 1, 1],
    [1, 1, 3, 2],
    [1, 2, 3, 1],
    [1, 1, 1, 4],
    [1, 3, 1, 2],
    [1, 2, 1, 3],
    [3, 1, 1, 2],
]


def abc():
    global multi, bin_pw
    rate = [0, 0, 0, 0]
    for i in bin_pw:
        if i == '0':
            if not rate[1]:
                rate[0] += 1
            else:
                rate[2] += 1
        else:
            if not rate[2]:
                rate[1] += 1
            else:
                rate[3] += 1
    if sum(rate) != 7:
        for i in range(4):
            rate[i] //= multi
    if rate in PASSWORD:
        real_pw = PASSWORD.index(rate)
        real_pws.append(real_pw)
        bin_pw.clear()
    else:
        multi += 1


def bbq():
    global real_pws
    Sum = 0
    for i in range(8):
        if i % 2 == 0:
            Sum += real_pws[i]
        else:
            Sum += 3 * real_pws[i]
    if Sum % 10 == 0:
        return sum(real_pws)
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        line = input().strip()
        if line.strip('0'):
            arr.append(line)

    checked = []
    pws = []
    ans = 0
    for s in arr:
        temp = s.strip('0')
        if temp and temp not in pws:
            pws.append(temp)

    pws.sort(key=len)
    for _ in range(2):
        for i in range(len(pws)):
            for j in range(len(pws)):
                if i != j:
                    if pws[i] in pws[j]:
                        pws[j] = pws[j].replace(pws[i], '')
                        pws[j] = pws[j].strip('0')
                    elif pws[j] in pws[i]:
                        pws[i] = pws[i].replace(pws[j], '')
                        pws[i] = pws[i].strip('0')

    for pw in pws:
        if not pw:
            continue
        real_pws = []
        num = int(pw, 16)
        flag = 0
        bin_pw = deque()
        multi = 1
        while num:
            check = num & 0x1
            num >>= 1
            if not flag:
                if check == 1:
                    flag = 1
                    bin_pw = deque(['1'])
            else:
                if check == 1:
                    bin_pw.appendleft('1')
                else:
                    bin_pw.appendleft('0')

            if len(bin_pw) % (7 * multi) == 0:
                if not bin_pw:
                    continue
                abc()

        if bin_pw and len(bin_pw) % 7 != 0:
            needed = (7 * multi) - len(bin_pw)
            for _ in range(needed):
                bin_pw.appendleft('0')
            if real_pws not in checked:
                checked.append(real_pws)
                abc()
                ans += bbq()

    print(f'#{tc} {ans}')