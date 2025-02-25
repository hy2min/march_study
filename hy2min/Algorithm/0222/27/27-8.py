s = input()
char = {}
for i in s:
    if i in char.values():
        char[i] += 1
    else:
        char[i] = 1
ret = sum(char.values())
print(f'{ret}종류')