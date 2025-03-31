arr = list(input())
stack = []

def abc(level):

    if level == 3:
        for i in range(len(stack)):
            print(arr[stack[i]],end='')
        print()
        stack.pop()
        return

    for i in range(4):
        if i in stack:
            continue
        else:
            stack.append(i)
            abc(level+1)
    if stack:
        stack.pop()

abc(0)