a=input()
n=ord(a)

for i in range(-3,4):
    if n+i>ord('Z'):
        print(chr(n+i-26),end='')
    elif n+i<ord('A'):
        print(chr(n+i+26),end='')
    else:
        print(chr(n+i),end='')