a,b = input().split()

arr = [ord(a) + i for i in range(ord(b)-ord(a)+1)]

for num in range(4):
    for i in arr:
        print(chr(i), end = ' ')
    print()