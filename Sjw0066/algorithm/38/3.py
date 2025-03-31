from collections import deque
arr=[list(map(int,input())) for _ in range(7)]
direct_y=[-1,1,0,0]
direct_x=[0,0,1,-1]
flag=1
q_shrimp=deque()
q_squid=deque()

for i in range(7):
    for j in range(7):
        if arr[i][j] == 1:
            q_shrimp.append((i,j))
        if arr[i][j] == 2:
            q_squid.append((i,j))

def check(y,x,power):
    global flag

    for i in range(4):
        for j in range(1,power+1):
            dy=y+j*direct_y[i]
            dx=x+j*direct_x[i]

            if dy>6 or dy<0 or dx<0 or dx>6:continue
            if arr[dy][dx] == power-1 :
                flag=0
                return
while q_shrimp:
    if flag==0:break
    a,b=q_shrimp.popleft()
    check(a,b,2)

while q_squid:
    if flag==0:break
    a,b=q_squid.popleft()
    check(a,b,3)

if flag:
    print('pass')
else:
    print('fail')