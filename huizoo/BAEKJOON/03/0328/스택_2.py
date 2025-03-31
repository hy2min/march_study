import sys
input = sys.stdin.readline

stack = []
N = int(input())
for _ in range(N):
    order = list(map(int, input().split()))
    if len(order) == 2:
        stack.append(order[1])
    else:
        order = order[0]
        if order == 2:
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif order == 3:
            print(len(stack))
        elif order == 4:
            if stack:
                print(0)
            else:
                print(1)
        else:
            if stack:
                print(stack[-1])
            else:
                print(-1)
