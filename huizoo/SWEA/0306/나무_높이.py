T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    Max = max(arr)
    even = 0
    odd = 0
    for i in range(N):
        while arr[i] <= Max - 2:
            arr[i] += 2
            even += 1
        if Max - arr[i] == 1:
            odd += 1
    ans = 0
    while even >= odd + 2:
        even -= 1
        odd += 2
    if odd - even in [0, 1]:
        ans = odd + even
    elif even - odd == 1:
        ans = odd + even + 1
    elif odd > even:
        gap = odd - even - 1
        ans = odd + even + gap
    print(f'#{tc} {ans}')
