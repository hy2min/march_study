from collections import deque
 
T=int(input())
for test_case in range(1,T+1):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    pizza=[]
    for i in range(m):
        pizza.append([i+1,arr[i]])
    oven=deque(pizza[:n])
    remain=deque(pizza[n:])
    while len(oven)>1:
        temp=oven.popleft()
        temp[1]//=2
        if temp[1]==0:
            if remain:
                oven.append(remain.popleft())
        else:
            oven.append(temp)
    print(f'#{test_case}',oven[0][0])