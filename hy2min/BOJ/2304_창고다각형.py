n = int(input())
lst = [0] * 1001
mx_i = mx = 0
for _ in range(n):
    l, h = map(int, input().split())
    lst[l] = h
    if mx < h:
        mx_i, mx = l, h
    
ans = mx = 0    
for i in range(mx_i+1):
    mx = max(mx, lst[i])
    ans += mx
mx = 0
for i in range(1000,mx_i,-1):
    mx = max(mx,lst[i])
    ans += mx

print(ans)
