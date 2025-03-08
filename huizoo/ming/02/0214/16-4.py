a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = [0]*4
for i in range(4):
    result[i] = a[i] + b[-i-1]
print(*result)