t = int(input())
for tc in range(1, t+1):
    n = int(input())

    stack = [[1]]
    
    for i in range(1,n):
        pre = stack[-1]
        new = [1]   
        for j in range(len(pre) -1):
            new.append(pre[j]+ pre[j+1])
        new.append(1)
        stack.append(new)

    print(f'#{tc}')
    for i in stack:
        print(*i)