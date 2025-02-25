n = int(input())

arr = []
for _ in range(n):
    s = input().split()
    if s[0] == 'push':
        arr.append(int(s[1]))
    if s[0] == 'printLast':
        print(arr[-1])
    if s[0] == 'pop':
        arr.pop()

