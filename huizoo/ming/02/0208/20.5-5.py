st = input()
n = ord(st)
for i in range(n-3, n+4) : 
    if i > ord('Z') : 
        i -= 26
    elif i < ord('A') : 
        i += 26
    print(chr(i), end='')