t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(input().split())

    ans = []
    if n % 2 == 0:
        a = arr[:n//2]
        b = arr[n//2:]
    else:
        a = arr[:n//2 +1]
        b = arr[n//2+1:]
    
    for i in range(n//2):
        ans.append(a[i])
        ans.append(b[i])
    if n % 2 == 1:
        ans.append(a[-1])
    
    print(f'#{tc} {" ".join(ans)}')