arr = [[0]* 5 for _ in range(5)]
A = 65
for i in range(5):
    for j in range(5):
        arr[i][j]  = chr(A)
        A += 1

s = input()
for i in range(5):
    for j in range(5):
        if arr[i][j] == s:
            y = i-2
            x = j-2
print(f'{y},{x}')
