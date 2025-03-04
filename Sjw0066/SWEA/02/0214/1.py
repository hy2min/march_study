def check(arr):
    for i in range(len(lst)):
        if lst[i] == '(' or lst[i] == '{':
            stack.append(lst[i])
        if lst[i] == ')':
            if stack:
                if stack.pop() != '(':
                    return 0
            else:
                return 0
        if lst[i] == '}':
            if stack:
                if stack.pop() != '{':
                    return 0
            else:
                return 0

    if stack:
        return 0
    else:
        return 1


T = int(input())

for tc in range(1, T + 1):
    lst = list(input())
    stack = []
    print(f'#{tc} {check(lst)}')