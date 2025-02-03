a,b = map(int,input().split())
arr = []

for i in range(3):
    arr.append(a+i)

for i in range(3):
    arr.append(b-2+i)

print(*arr)