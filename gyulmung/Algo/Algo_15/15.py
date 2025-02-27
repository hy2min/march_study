arr = [[0]*8 for _ in range(2)]
for i in range(2):
    string = input()
    for j in range(len(string)):
        arr[i][j]=string[j]

count = 0
for i in range(8):
    if arr[0][i] != arr[1][i]:
        count += 1

print(count)