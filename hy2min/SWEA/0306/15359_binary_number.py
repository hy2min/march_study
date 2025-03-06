t = int(input())
hex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

for tc in range(1, t+1):
    n, num = input().split()
    n = int(n)
    bi = []
    for i in range(n):
        check = hex.index(num[i])
        binary = [0,0,0,0]
        while check > 0:
            k = 3
            binary[k] = check % 2
            check //= 2
            k -= 1
        bi.extend(binary)
    print(f'#{tc} {"".join(map(str,bi))}')