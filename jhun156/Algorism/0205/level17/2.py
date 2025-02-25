arr = [5,9,4,6,1,5,8,9]

a,b = map(int,input().split())

for i in range(a,8):
    if arr[i] == b:
        tmp = i
result = tmp - a
print(result)