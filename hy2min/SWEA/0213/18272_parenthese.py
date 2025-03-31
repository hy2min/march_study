def abc(s):
    stack = []  
    for i in s:
        if i in "({":
            stack.append(i)
        elif i in ')}':
            if not stack:
                return 0
            last = stack.pop()
            if (last =='(' and i != ')') or (last =='{' and i != '}'):
                return 0
    return 1 if not stack else 0

t = int(input())
for tc in range(1, t+1):
    s = input()
    ans = abc(s)
    print(f'#{tc} {ans}')