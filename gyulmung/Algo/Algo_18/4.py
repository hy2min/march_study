arr = list(map(str, input()))

lst = [0]*15
count = 0
for i in range(len(arr)):
    lst[ord(arr[i]) - 65] += 1

for i in range(15):
    if lst[i] != 0:
        count += 1

print(f'{count}개')