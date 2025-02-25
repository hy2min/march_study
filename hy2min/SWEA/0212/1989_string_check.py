T = int(input())
for idx in range(T):
    s = input().strip()

    if s == s[::-1]:
        print(f'#{idx+1} 1')
    else:
        print(f'#{idx+1} 0')


