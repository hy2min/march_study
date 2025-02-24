for tc in range(1, 11):
    n = int(input())
    st = input()
    result = ""
    stack = []
    priority = {'+': 1, '*': 2}
    for i in st:
        if i.isdigit():
            result += i
        else:
            # new새로 들어올 값 stack에 있는값이랑 비교
            if stack and priority[i] <= priority[stack[-1]]:
                result += (stack.pop())
            stack.append(i)

    while stack:
        result += stack.pop()

    # 2 후위표기식 계산
    for i in result:
        if i.isdigit():
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            if i == '*': stack.append(a * b)
            if i == '+': stack.append(a + b)

    print(f'#{tc} {stack.pop()}')