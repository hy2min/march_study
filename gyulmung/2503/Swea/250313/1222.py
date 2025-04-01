import sys
sys.stdin = open('input.txt','r')

from collections import deque
T = 1

for test in range(1, T+1):
    N = int(input())
    arr = input()
    print(arr)

    result = ''
    stack = []
    # 전위표기식 후위표기식으로 바꾸기
    for i in arr:
        if i.isdigit():
            result += i
        else:
            if stack:
                result += stack.pop()
                stack.append(i)
            else:
                stack.append(i)
    result+=stack.pop()

    # 후위표기식 계산하기
    for i in result:
        if i.isdigit():
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
    ans = stack.pop()
    print(f'#{test} {ans}')

