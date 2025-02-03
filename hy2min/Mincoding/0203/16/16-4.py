a = [0] * 4
b = [0] * 4

a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = []
for i in range(4):
    result.append(a[i] + b[::-1][i])

for i in result:
    print(i, end=" ")