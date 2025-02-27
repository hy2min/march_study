from collections import deque
 
T=int(input())
for test_case in range(1,T+1):
    n,m=map(int,input().split())
    q=deque()
    arr=list(map(int,input().split()))
    for i in range(n):
        q.append(arr[i])
    for i in range(m):
        q.rotate(-1)
    lst=list(q)
 
    print(f'#{test_case}',lst[0])