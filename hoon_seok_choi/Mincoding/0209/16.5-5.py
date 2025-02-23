a = input()

arr = [*a]

for i in range(len(arr)) :
    arr[i] = ord(arr[i])

min_v = min(arr)
max_v = max(arr)

b= arr.index(min_v)
c= arr.index(max_v)

print(c)
print(b)
