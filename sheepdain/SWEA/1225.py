from collections import deque
 
T=10
for test_case in range(1,T+1):
    tc=int(input())
    q=deque(list(map(int,input().split())))
    idx=[1,2,3,4,5]
    while q[-1]>0:
        for i in idx:
            n=q.popleft()
            q.append(n-i)
            if q[-1]<=0:
                q[-1]=0
                break
    print(f'#{tc}',*list(q))