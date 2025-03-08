arr = [[0]*5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        arr[i][j] = chr(65+j+5*i)
alp = input()
for i in range(5):
    for j in range(5):
        if arr[i][j] == alp:
           y, x = i, j

print(f'{y-2},{x-2}')