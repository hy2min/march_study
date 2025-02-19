s = input()
for i in range(-3,4):
    a = ord(s) + i
    if a > 90:
        a -= 26
    if a < 65:
        a += 26

    print(chr(a), end="")

