import sys
sys.stdin = open("input.txt", "r")

def find_pw():
    for i in range(n):
        for j in range(m - 1, -1, -1):
            if arr[i][j] == '1':
                return i, j

t = int(input())
pw = [
    '0001101',
    '0011001',
    '0010011',
    '0111101',
    '0100011',
    '0110001',
    '0101111',
    '0111011',
    '0110111',
    '0001011',
]
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    y, x = find_pw()
    even = 0
    odd = 0
    n = 1
    for i in range(x-55, x+1, 7):
        pw2 = pw.index(arr[y][i:i+7])
        if n:
            odd += pw2
            n -= 1
        else:
            even += pw2
            n += 1


    if (even + 3*odd) % 10 == 0:
        print(f'#{tc} {even+odd}')
    else:
        print(f'#{tc} 0')