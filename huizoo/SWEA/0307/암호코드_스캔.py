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
    # print(bin_pw)
    if sum(rate) != 7:
        for i in range(4):
            rate[i] //= multi
    if rate in PASSWORD:
        real_pw = PASSWORD.index(rate)
        real_pws.append(real_pw)
        bin_pw = ''
    else:
        multi += 1
    # print(rate)

def bbq():
    global real_pws
    Sum = 0
    for i in range(8):
        if i % 2 == 0:
            Sum += real_pws[i]
        else:
            Sum += 3*real_pws[i]
    if Sum % 10 == 0:
        return sum(real_pws)
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    if tc == 8:
        debug = 1
    if tc == 13:
        debug = 1
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    checked = []
    pws = []
    ans = 0
    for i in range(N):
        temp = arr[i].strip('0')
        if temp and temp not in pws:
            pws.append(temp)
    # pws2 = []
    # for pw in pws:
    #     exist = 0
    #     for pw2 in pws2:
    #         if pw2 in pw:
    #             exist = 1
    #             continue
    #     if exist:
    #         continue
    #     else:
    #         pws2.append(pw)


    for pw in pws:
        print(f'길이 :{len(pw)}')
        real_pws = []
        num = int(pw, 16)
        # print(bin(num))
        flag = 0
        bin_pw = ''
        # print(f'num : {num}')
        multi = 1
        while num:
            if bin_pw == '0':
                bin_pw = ''
            check = num & 0x1
            if not flag:
                if check == 0:
                    num = num >> 1
                if check == 1:
                    flag = 1
                    bin_pw = '1' + bin_pw
                    num = num >> 1
            else:
                if check == 1:
                    bin_pw = '1' + bin_pw
                    num = num >> 1
                else:
                    bin_pw = '0' + bin_pw
                    num = num >> 1

            if len(bin_pw) % (7*multi) == 0:
                if not bin_pw: continue
                abc()
                if len(real_pws) == 8 and real_pws not in checked:
                    checked.append(real_pws)
                    ans += bbq()

                # print(bin(num))
        if bin_pw and len(bin_pw) % 7 != 0:
            bin_pw = (7*multi - len(bin_pw))*'0' + bin_pw
            if real_pws not in checked:
                abc()
                ans += bbq()
        # print(bin_pw)
        # print(real_pws)
        # print(f'현재답 {ans}')
    print(f'#{tc} {ans}')






