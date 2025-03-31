n = int(input())
arr = [list(input().split()) for _ in range(n)]

arr.sort(key=lambda x:(int(x[0]),x[1]))

for i in arr:
    print(*i)