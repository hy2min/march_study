def inorder(now):
    global ans
    if now >= len(arr) or arr[now] == 0:
        return
    inorder(now*2)
    ans += arr[now]
    inorder(now * 2 +1)


t = 10
for tc in range(1, t+1):
    n = int(input())
    arr = [0] * (n+1)
    for _ in range(n):
        node, value, *etc = input().split()
        node = int(node)
        arr[node] = value
    ans = ''
    inorder(1)
    print(f'#{tc} {ans}')