arr = [i for i in map(int,input().split())]

for i in range(1,6,2):
    arr[i] = 21e8

ans = min(arr)
for i in range(6):
    if arr[i] == ans:
        print(f"arr[{i}]={ans}")