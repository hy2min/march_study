a = input()

# print(ord("A"),ord("Z")) 65 90

lst = []
for i in range(-3,4):
    if ord(a) + i < 65:
        lst.append(ord(a)+i+26)
    elif ord(a) + i > 90:
        lst.append(ord(a)+i-26)
    else:
        lst.append(ord(a)+i)
for i in range(7):
    print(chr(lst[i]),end='')