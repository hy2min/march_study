# import sys
# sys.stdin = open("input.txt","r")

def dfs(n):

    global stack
    if n > 1000:
        return
    if arr[n] == -1:
        return

    if type(arr[n]) == float or type(arr[n]) == int:
        stack.append(float(arr[n]))
    else:
        stack.append(arr[n][0])
        dfs(arr[n][1])
        dfs(arr[n][2])
        a = stack.pop()
        b = stack.pop()
        c = stack.pop()
        if c == '+':
            tmp = a + b
            stack.append(tmp)
        elif c == '-':
            tmp = b - a
            stack.append(tmp)
        elif c == '*':
            tmp = b * a
            stack.append(tmp)
        elif c == '/':
            tmp = b / a
            stack.append(tmp)

T = 10
for tc in range(1,T+1):
    N = int(input())
    arr = [-1] * 1001
    for _ in range(N):
        lst = list(input().split())
        if len(lst) == 2:
            arr[int(lst[0])] = int(lst[1])
        elif len(lst) == 4:
            arr[int(lst[0])] = [lst[1],int(lst[2]), int(lst[3])]

    stack = []
    dfs(1)
    print(f"#{tc} {int(stack[0])}")
