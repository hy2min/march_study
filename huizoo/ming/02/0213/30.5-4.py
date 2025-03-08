arr = [input() for _ in range(3)]
longest = ['']
long_len = -1
for i in range(3):
    if len(arr[i]) > len(longest[0]):
        longest = [arr[i]]
        long_len = len(arr[i])
    elif len(arr[i]) == len(longest[0]):
        longest.append(arr[i])

if len(longest) > 1:
    print(max(longest))
else:
    print(*longest)