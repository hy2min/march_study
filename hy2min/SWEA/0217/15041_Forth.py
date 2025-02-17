#
#
# def cal(lst):
#     stack = []
#     for s in lst:
#         if s.isdigit():
#             stack.append(int(s))
#         elif s == '.':
#             if stack:
#                 return stack.pop()
#             else:
#                 return 'error'
#         else:
#             if len(stack) < 2:
#                 return 'error'
#             a = stack.pop()
#             b = stack.pop()
#
#             if s == "+":
#                 stack.append(b + a)
#             elif s == "-":
#                 stack.append(b - a)
#             elif s == "*":
#                 stack.append(b * a)
#             elif s == "/":
#                 if a == 0:
#                     return 'error'
#                 stack.append(b // a)
#             else:
#
#                 return 'error'
#
#     if stack:
#         return 'error'

T = int(input())
for idx in range(T):
    lst = input().split()

    stack = []

    try:
        for s in lst:
            if s.isdigit():
                stack.append(int(s))

            elif s == '.':
                if len(stack) == 1:
                    print(f'#{idx+1} {stack.pop()}')
                else:
                    print(f'#{idx+1} error')
            elif s in ['+','-','*','/']:
                b = stack.pop()
                a = stack.pop()

                if s == '+':
                    stack.append(a+b)
                elif s == '-':
                    stack.append(a-b)
                elif s == '*':
                    stack.append(a*b)
                elif s == '/':
                    stack.append(a//b)
    except:
        print(f'#{idx+1} error')
