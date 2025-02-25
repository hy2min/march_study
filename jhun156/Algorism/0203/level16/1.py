arr = [[0] * 10 for _ in range(3)]

a = input()
b = input()
c = input()
lst = [a,b,c]

for i in range(3):
    for j in range(len(lst[i])):
        arr[i][j] = lst[i][j]

for i in range(3):
    for j in range(10):
        if arr[i][j] == 0:
            print(arr[i][j-1],end='')
            break