n = int(input())

arr = list(input() for _ in range(n))

arr.sort(key=lambda x: (len(x),x))

for i in arr:
    print(i)