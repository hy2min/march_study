a,b = map(int,input().split())

arr = [a + i * b for i in range(5)]

print(*arr)