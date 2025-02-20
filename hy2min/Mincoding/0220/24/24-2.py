name = input()
n = int(input())
for _ in range(n):
    s = input()
    if name in s:
        print('O')
    else:
        print('X')