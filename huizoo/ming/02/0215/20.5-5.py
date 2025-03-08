a = input()
for i in range(-3, 4):
    if ord(a)+i > 90:
        print(chr(ord(a)+i-26), end='')
    elif ord(a)+i < 65:
        print(chr(ord(a)+i+26), end='')
    else:
        print(chr(ord(a) + i), end='')
        
