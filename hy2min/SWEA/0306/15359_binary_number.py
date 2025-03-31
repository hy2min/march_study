def hex2bin(n):
    bin_n = ''
    while n != 0:
        bin_n = str(n % 2) + bin_n
        n //= 2

    while len(bin_n) < 4:
        bin_n = '0' + bin_n
    return bin_n

hex = "0123456789ABCDEF"

t = int(input())
for tc in range(1, t+1):
    n, num = input().split()

    ans = ''
    for i in num:
        hex_n = hex.index(i)
        ans += hex2bin(hex_n)
    print(f'#{tc} {ans}')
# hex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

# for tc in range(1, t+1):
#     n, num = input().split()
#     n = int(n)
#     bi = []
#     for i in range(n):
#         check = hex.index(num[i])
#         binary = [0,0,0,0]
#         while check > 0:
#             k = 3
#             binary[k] = check % 2
#             check //= 2
#             k -= 1
#         bi.extend(binary)
#     print(f'#{tc} {"".join(map(str,bi))}')