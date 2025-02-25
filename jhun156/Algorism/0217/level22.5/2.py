arr = ['x','o']
stack = []
n = int(input())

def abc(level):

    if level == n:
        for i in range(len(stack)):
            print(arr[stack[i]],end='')
        print()
        stack.pop()
        return

    for i in range(2):
        stack.append(i)
        abc(level+1)
    if stack:
        stack.pop()

abc(0)