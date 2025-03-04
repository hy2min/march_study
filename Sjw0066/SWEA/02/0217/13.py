T=int(input())

for tc in range(1,T+1):
    lst=list(input().split())
    stack=[]
    try:
        for i in lst:
            if i.isdigit():
                stack.append(int(i))

            elif i in ['+','-','*','/']:
                b=stack.pop()
                a=stack.pop()

                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(a-b)
                elif i == '*':
                    stack.append(a*b)
                elif i == '/':
                    stack.append(a//b)

            elif i == ".":
                if len(stack) == 1:
                    print(f'#{tc} {stack.pop()}')
                else:
                    print(f'#{tc} error')
    except:
        print(f'#{tc} error')