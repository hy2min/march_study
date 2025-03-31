arr = list(str(input()))
num = int(input())
arr.insert(num, 'A')
print(*arr, sep = '')