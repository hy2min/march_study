from collections import deque
for tc in range(1, 11):
    N = int(input())
    st = deque(list(input()))
    st2 = [st.popleft()]
    temp = []
    for _ in range((N-1)//2):
        a = st.popleft()
        b = st.popleft()
        if a == '+':
            if st and st[0] == '*':
                temp.append(a)
                temp.append(b)
            else:
                st2.append(b)
                st2.append(a)
        elif a == '*':
            if st and st[0] == '*':
                temp.append(a)
                temp.append(b)
            else:
                temp1 = []
                temp2 = []
                while temp:
                    temp1.append(temp.pop())
                    temp2.append(temp.pop())
                st2 += temp1[::-1]
                st2.append(b)
                st2.append(a)
                st2 += temp2

    st2 = deque(st2)
    stack = []
    for _ in range(N):
        a = st2.popleft()
        if a.isdecimal():
            stack.append(int(a))
        else:
            n2 = stack.pop()
            n1 = stack.pop()
            if a == '*':
                stack.append(n1*n2)
            elif a == '+':
                stack.append(n1+n2)
    print(f'#{tc}', stack[0])
