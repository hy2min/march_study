value = int(input())
n = int(input())

for i in range(n):
    value *= 2
    value = int(str(value)[::-1])

print(value)
