arr = list(map(int, input().split()))

a = sorted(arr)[::-1]

for i in range(len(a)) :
    print(a[i], end="")