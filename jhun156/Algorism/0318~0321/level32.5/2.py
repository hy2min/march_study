arr = list(input())
for i in range(len(arr)):
    arr[i] = ord(arr[i])

while True:

    for i in range(len(arr)):
        if type(arr[i]) == int:
            print(chr(arr[i]),end='')
        else:
            print(arr[i],end='')
    print()
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == '_':
            arr[i] = '_'
            cnt += 1
        elif arr[i] == ord('A'):
            arr[i] = '_'
        else:
            arr[i] -= 1

    if cnt == len(arr):
        break