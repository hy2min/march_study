import sys
sys.stdin = open("input.txt", "r")

def abc(st):
    num = int(st, 3)

    for i in range(n):
        if N[i] == '1':
            if num == int(N[:i]+'0'+N[i+1:], 2):
                return num
        else:
            if num == int(N[:i]+'1'+N[i+1:], 2):
                return num

    return 0

T = int(input())
for tc in range(1, T+1):
    N = input()
    M = input()
    n = len(N)
    m = len(M)

    for i in range(m):
        if i == '0':
            if M[0] == '2':
                ret = abc('1'+M[i+1:])
            else:
                ret = abc('2'+M[i+1:])
            if ret:
                break
        else:
            if M[i] == '0':
                ret = max(abc(M[:i]+'1'+M[i+1:]), abc(M[:i]+'2'+M[i+1:]))
                if ret:
                    break
            elif M[i] == '1':
                ret = max(abc(M[:i]+'0'+M[i+1:]), abc(M[:i]+'2'+M[i+1:]))
                if ret:
                    break
            else:
                ret = max(abc(M[:i]+'0'+M[i+1:]), abc(M[:i]+'1'+M[i+1:]))
                if ret:
                    break

    print(f'#{tc} {ret}')
