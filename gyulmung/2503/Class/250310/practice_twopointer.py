n, m = map(int, input().split())

arr = list(map(int, input().split()))
L, R = 0, 0
count = 0
for i in range(n*2-1):
    if sum(arr[L:R]) == m:
        count += 1
    if sum(arr[L:R]) < m:
        R += 1
    elif sum(arr[L:R]) or R == n >= m:
        L += 1
    elif L == n and R == n:
        break
print(count+1)

# 강사님 코드

n,m=map(int,input().split())       # 11 5
arr=list(map(int,input().split())) # 1 2 3 4 2 5 3 1 1 2 5
cnt,Sum=0,0
right,left=0,0
target=m
while 1:
    if Sum>=target or right==n:
        Sum-=arr[left]
        left+=1
    elif Sum<target:
        Sum+=arr[right]
        right+=1
    if Sum==target:
        cnt+=1
    if left==n:
        break
print(cnt)