T = 10
for idx in range(10):
    ans = 0

    n = int(input())
    s = input()

    result = ""
    stack = []

    priority = {'+': 1, '*': 2}
    for i in s:
        if i.isdigit():
            result += i
        else:
            if stack and priority[i] <=priority[stack[-1]]:
                result += stack.pop()
            stack.append(i)

    while stack:
        result += stack.pop()

    for i in result:
        if i.isdigit():
            stack.append(i)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if i == '+':
                stack.append(a+b)
            elif i == '*':
                stack.append(a*b)
    ans = stack.pop()


    print(f'#{idx+1} {ans}')