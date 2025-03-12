n = int(input())
arr = [input() for _ in range(n)]
for i in range(n):
    if arr[i].istitle():
        continue
    elif arr[i].islower():
        arr[i] = arr[i].capitalize()
    else:
        arr[i] = arr[i].upper()
arr.sort()
for i in arr:
    print(i)
