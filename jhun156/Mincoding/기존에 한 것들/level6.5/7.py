arr = [i for i in input().split()]
arr2 = []

for i in arr:
    if i.isupper():
        arr2.append(i.lower())
    elif i.islower():
        arr2.append(i.upper())

print(*arr2)