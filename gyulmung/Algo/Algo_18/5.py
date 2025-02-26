arr = list(map(str, input()))

lst = [0]*26
Max = -1e8

for i in range(len(arr)):
    lst[ord(arr[i]) - 65] += 1
    if Max < lst[ord(arr[i]) - 65]:
        Max = lst[ord(arr[i]) - 65]
        check_char = arr[i]

print(check_char)