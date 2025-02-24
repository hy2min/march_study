st = list(input())
a, b = input().split()
for i in range(len(st)):
    if st[i] == a:
        if i - 1 >= 0:
            st[i - 1] = '#'
        if i + 1 < len(st):
            st[i + 1] = '#'
    elif st[i] == b:
        if i - 1 >= 0:
            st[i - 1] = '#'
        if i + 1 < len(st):
            st[i + 1] = '#'
print(*st, sep='')