def postorder(x):
    if x > N: return
    info = arr[x]
    if info[0].isdecimal():
        return int(info[0])
    else:
        left = postorder(int(info[1]))
        right = postorder(int(info[2]))
        if info[0] == '-':
            return left - right
        elif info[0] == '*':
            return left * right
        elif info[0] == '/':
            return left / right
        else:
            return left + right

for tc in range(1, 11):
    N = int(input())
    arr = [0]*(N+1)
    for _ in range(N):
        a, *b = input().split()
        arr[int(a)] = b

    print(f'#{tc} {int(postorder(1))}')