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

def abc(x):
    pw = []
    now = '1'
    while len(pw) < 3:
        cnt = 0
        for i in range(x, length):
            if row[i] == now:
                cnt += 1
            else:
                break
        x += cnt
        pw.append(str(cnt))
        if now == '1':
            now = '0'
        else:
            now = '1'

    return PASSWORD[''.join(pw)], x


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip('0') for _ in range(N)]
    for row in arr:
        if row:
            length = len(row)
            check = [0]*length
            nums = []
            for i in range(length):
                if check[i]: continue
                if row[i] != '1': continue
                ret = abc(i)
                nums.append(ret[0])
                for j in range(i, ret[1]):
                    check[j] = 1
            if nums:
                password = 0
                for i in range(0, 8, 2):
                    password += nums[i]*3
                for i in range(1, 8, 2):
                    password += nums[i]
                if password % 10 == 0:
                    print(f'#{tc} {sum(nums)}')
                else:
                    print(f'#{tc} 0')
                break
