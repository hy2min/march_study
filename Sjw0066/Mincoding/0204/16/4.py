a = list(map(int,input().split()))
b = list(map(int,input().split()))

result=[0]*4
for i in range(4):
    result[i] = a[i] + b[3-i]

print(*result)