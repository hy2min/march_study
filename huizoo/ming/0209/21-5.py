arr = [list(input()) for _ in range(3)]

longest = []

for i in range(3) : 
    if len(longest) < len(arr[i]) : 
        longest = arr[i]
        longest_index = i

temp = arr[0]
arr[0] = longest
arr[longest_index] = temp

print('\n'.join(''.join(map(str, row))for row in arr))