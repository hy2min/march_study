st = list(input())
n = len(st)
print(*st, sep='')
while ''.join(st) != '_'*n:
    for i in range(n):
        asc = ord(st[i])
        if 65 < asc <= 90:
            st[i] = chr(asc-1)
        elif asc == 65:
            st[i] = '_'
    print(*st, sep='')