T = int(input())
arr = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
       '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
for tc in range(1, T+1):
    n, a = input().split()
    ans = ''
    for i in a:
        if i.isdecimal():
            ans += arr[int(i)]
        else:
            ans += arr[int(10+ord(i)-ord('A'))]
    print(f'#{tc} {ans}')