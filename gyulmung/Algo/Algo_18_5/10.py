string = list(map(str, input()))
lst = [0]*26


for i in range(len(string)):
    lst[ord(string[i])-65] += 1

for i in range(len(lst)):
    if lst[i] >= 1:
        print(f'{chr(i + 65)}:{lst[i]}')
