T = int(input())
for idx in range(T):
    N = int(input())
    arr = (input().split('0'))

    max_len = 0
    for i in arr:
        if len(i) > max_len:
            max_len = len(i)

    print(f'#{idx+1} {max_len}')