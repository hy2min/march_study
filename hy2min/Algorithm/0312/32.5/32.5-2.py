s = list(input())

num = [ord(i) for i in s]
while any(i >= 65 for i in num):
    for i in num:
        if i >= 65:
            print(chr(i),end="")
        else:
            print('_',end="")
    print()

    for i in range(len(s)):
        if num[i] < 65:
            continue
        else:
            num[i] -= 1

print("_" * len(s))