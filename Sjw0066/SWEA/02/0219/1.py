from collections import deque


T=10
for tc in range(1,T+1):

    tc=int(input())
    lst=list(map(int,input().split()))
    q = deque(lst)

    flag=0

    while 1:

        for i in range(1,6):
            a = q.popleft()
            a=a-i
            if a<=0:
                a=0
                flag=1
                q.append(a)
                break
            q.append(a)

        if flag:
            break

    print(f'#{tc}',end=" ")
    print(*list(q))

