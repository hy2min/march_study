import sys
sys.stdin = open('input.txt', 'r')

def abc(i):
    if i > N:
        return
    if type(arr[i]) is int:
        stack.append(arr[i])
        return
    else:
        abc(int(arr[i][1]))
        abc(int(arr[i][2]))
        right = stack.pop()
        left = stack.pop()
        if arr[i][0] == '-':
            stack.append(left - right)
        elif arr[i][0] == '+':
            stack.append(left + right)
        elif arr[i][0] == '*':
            stack.append(left * right)
        else:
            stack.append(left / right)

for tc in range(1, 11):
    N = int(input())
    arr = [0] * (N+1)
    for i in range(1, N+1):
        temp = list(input().split())
        if temp[1].isdecimal():
            arr[i] = int(temp[1])
        else:
            arr[i] = tuple(temp[1:])
    stack = []

    abc(1)
    print(f'#{tc} {int(stack[0])}')