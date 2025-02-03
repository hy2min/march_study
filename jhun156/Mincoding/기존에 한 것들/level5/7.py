arr = [i for i in map(int,input().split())]

a = int(input())

for i in range(3):
    arr.append(a+i)

print(*arr)