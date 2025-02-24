def abc(lst):
    for char in lst:
        if char == '(':
            path.append('(')
        elif char == '{':
            path.append('{')
        elif char == ')':
            if not path:
                return 0
            else:
                if path[-1] == '(':
                    path.pop()
                elif path[-1] == '{':
                    return 0
        elif char == '}':
            if not path:
                return 0
            else:
                if path[-1] == '{':
                    path.pop()
                elif path[-1] == '(':
                    return 0
    if path:
        return 0
    return 1

t = int(input())
for tc in range(1, t+1):
    arr = list(input())
    path = []
    ans = abc(arr)
    print(f'#{tc} {ans}')


