# import sys
# sys.stdin = open("input.txt","r")

code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    y,x = 0,0
    flag = 0
    for i in range(N):
        for j in range(M-7):
            tmp = ''
            for k in range(7):
                tmp += arr[i][j+k]
            if tmp in code:
                ret = ''
                for w in range(7):
                    ret += arr[i][j+7+w]
                if ret in code:
                    y,x = i,j
                    flag = 1
                    break
            if flag:
                break
        if flag:
            break

    lst = []
    for i in range(0,56,7):
        tmp = ''
        for j in range(7):
            tmp += arr[y][x+i+j]
        lst.append(code[tmp])

    ans = 0
    result = 0
    for i in range(8):
        if i % 2 == 0:
            result += 3 * lst[i]
            ans += lst[i]
        else:
            result += lst[i]
            ans += lst[i]

    if result % 10 == 0:
        print(f"#{tc} {ans}")
    else:
        print(f"#{tc} 0")