N = int(input())
arr = []
for i in range(N):
    arr.append(input())

arr.sort(key = lambda x: (len(x),x))
for i in range(N):
    print(arr[i])