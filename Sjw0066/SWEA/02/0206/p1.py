T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input()))


    dat = [0] * 10 #숫자개수를 받기 위한 배열 생성
    max_num = -1e21
    for i in range(len(ai)):
        dat[ai[i]] += 1
        if max_num < ai[i]:
            max_num = ai[i]

    max_dat = -1e21
    num1 = 0
    for i in range(len(dat)):
        if max_dat <= dat[i]:
            max_dat = dat[i]
            num1 = i


    print(f'#{tc} {num1} {max_dat}')
