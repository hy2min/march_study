arr = ['A','B','C','D']
result_lst = []
stack = []

def abc(level):

    global arr,result_lst,stack

    if level == 3:
        a = ''
        for i in range(3):
            a += arr[stack[i]]
        result_lst.append(a)
        stack.pop()
        return

    for i in range(4):
        stack.append(i)
        abc(level+1)
    if stack:
        stack.pop()

abc(0)
a = input()
ans = 0
for i in range(len(result_lst)):
    if result_lst[i] == a:
        ans = i + 1
        break
print(f"{ans}번째")