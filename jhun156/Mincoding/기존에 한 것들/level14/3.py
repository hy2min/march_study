a,b = map(int,input().split())
count = 0

if a < b:
    while a < 100:
        count += 1
        a += 1
else:
    while b < 100:
        count += 1
        b += 1
print(count)
