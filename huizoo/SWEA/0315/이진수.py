T = int(input())
for tc in range(1, T+1):
    n, h = input().split()
    h = bin(int(h, 16))[2:]
    print(f'#{tc} {"0"*(4*int(n) - len(h)) + h}')