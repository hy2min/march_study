a = input()

arr = [ord('A')+ i for i in range(ord(a)-ord('A')+1)]

for i in arr:
    print(chr(i),end='')
