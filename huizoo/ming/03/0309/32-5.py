n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
arr.sort(key=lambda x: (len(x), x))
print('\n'.join(arr))