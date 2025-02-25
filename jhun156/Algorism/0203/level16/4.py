list_a = [i for i in map(int,input().split())]
list_b = [i for i in map(int,input().split())]

result = [0] * 4

for i in range(4):
    result[i] = list_a[i] + list_b[3-i]

print(*result)