a = input()

arr1 = [ord(a) + i for i in range(5)]
arr2 = [ord(a) - i for i in range(5)]

for i in arr1:
    print(chr(i),end='')

print()

for i in arr2:
    print(chr(i),end='')

