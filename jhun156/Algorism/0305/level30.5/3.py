arr = [1,5,4,2,-5,-7]
n = int(input())
arr.sort()

cnt = 0
while cnt < n - 1:
    arr.pop()
    cnt += 1

print(arr.pop())