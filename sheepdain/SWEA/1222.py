testcase = 10
for tc in range(1, testcase + 1):
    ans = 0
    n = int(input())
    str = input()
    result = ''
    stack = []
    for i in str:
        if i.isdigit():
            result += i
        else:
            if stack:
                result += stack.pop() 
                stack.append(i)  
            else:
                stack.append(i)
    result += stack.pop()  
 
    for i in result:
        if i.isdigit():
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
    ans = stack.pop()
 
    print(f'#{tc}', ans)