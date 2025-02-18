t = int(input())
for tc in range(1, t+1):
    arr = list(input().split())
    stack = []
    flag = 0
    try:
        for _ in range(len(arr)):
            a = arr.pop(0)
            if a == '.':
                flag = 1
            if a.isdecimal():
                stack.append(int(a))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                if a == '*':
                    stack.append(n1*n2)
                elif a == '+':
                    stack.append(n1+n2)
                elif a == '-':
                    stack.append(n1-n2)
                elif a == '/':
                    stack.append(n1/n2)
    except:
        print(f'#{tc} error')
    if flag:
        print(f'#{tc} {stack.pop()}')