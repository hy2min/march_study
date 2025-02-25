lst = ['B','G','T','K']
n = int(input())
stack = []

def abc(level):

    global lst,n
    if level == n:
        for i in range(len(stack)):
            print(lst[stack[i]],end='')
        print()
        stack.pop()
        return

    for i in range(4):
        stack.append(i)
        abc(level+1)
    if stack:
        stack.pop()

abc(0)