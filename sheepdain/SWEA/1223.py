T = 10
for test_case in range(1, T + 1):
    ans=0
    n=int(input())
    str=input()
    result=''
    stack=[]
    priority={'+':1,'*':2}
    for i in str:
        if i.isdigit():
            result+=i
        else:
            if stack and priority[i]<=priority[stack[-1]]:
                result+=(stack.pop())
            stack.append(i)
    while stack:
        result+=stack.pop()
 
    for i in result:
        if i.isdigit():
            stack.append(int(i))
        else:
            a=stack.pop()
            b=stack.pop()
            if i=='*': stack.append(a*b)
            if i=='+': stack.append(a+b)
    ans=stack.pop()
    print(f'#{test_case}',ans)