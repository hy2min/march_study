arr=[list(map(int,input())) for _ in range(5)]
a,b=map(int,input().split())

arr[a].sort()
arr[b].sort()

for i in arr:
    print(i[0],end=" ")