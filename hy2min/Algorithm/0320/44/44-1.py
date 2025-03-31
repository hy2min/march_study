data = {}

n = int(input())
for _ in range(n):
    name, age = input().split()
    if name in data:
        print(name)
        print(data[name], end=" ")
        print(age)
    else:
        data[name] = age