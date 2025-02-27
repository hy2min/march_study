string = list(map(str, input()))
lst = [0]*26
Max = -1e8

for i in range(len(string)):
    lst[ord(string[i])-65] += 1

for i in range(len(lst)):
    if Max < lst[i]:
        Max = lst[i]
        Alpha = i

print(chr(Alpha + 65))