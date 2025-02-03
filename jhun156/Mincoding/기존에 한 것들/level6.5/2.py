a = input()

arr = [ord(a) - i for i in range(ord(a)-ord('a')+1)]

for i in arr:
    print(chr(i),end='')