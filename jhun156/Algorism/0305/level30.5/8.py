arr = ['B','I','A','H']
n = int(input())
index = 0

while arr:
    k = len(arr)
    index = (n + index - 1) % k
    print(arr.pop(index),end=' ')
