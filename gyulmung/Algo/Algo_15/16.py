char = input()

count1 = 1

arr = [[0]*3 for _ in range(3)]

while count1 < 4:
    count2 = 0
    while count2 < count1:
        arr[3 - count1][count2] = char
        count2 += 1
        char = chr(ord(char) + 1)
    count1 += 1

for i in range(3):
    for j in range(3):
        print(arr[i][j] if arr[i][j] != 0 else '', end = '')
    print()
