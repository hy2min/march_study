def abc(n):
    if path == []:
        for i in range(n, length):
            if arr[i] == '(':
                path.append('(')
                abc(i)
                path.pop()
                pass
            elif arr[i] == '{':
                pass
    elif path[0] == '(':
        for i in range(n, length):

        pass

    return

t = int(input())
for tc in range(1, t+1):
    arr = list(input())
    length = len(arr)
    path = []
    abc(0, arr)
    print(f'#{tc} ')