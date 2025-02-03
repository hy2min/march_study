arr = []

for i in map(int,input().split()):
    arr.append(i)

count = 0

for i in arr:
    if i >= 3 and i <= 7:
        count += 1

print(count)