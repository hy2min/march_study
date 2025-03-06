t = int(input())
for tc in range(1, t+1):
    arr = input().split()
    stack = []
    try:
        for i in arr:
            if i == '.':
                if len(stack) == 1:
                    print(f'#{tc} {stack.pop()}')
                else:
                    print(f'#{tc} error')
            elif i.isdecimal():
                stack.append(int(i))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if i == '*': stack.append(n1*n2)
                elif i == '+': stack.append(n1+n2)
                elif i == '-': stack.append(n1-n2)
                elif i == '/': stack.append(n1//n2)
    except:
        print(f'#{tc} error')
