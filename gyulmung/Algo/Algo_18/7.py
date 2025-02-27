arr =  [['A', 'B', 'C'],
        ['A', 'G', 'H'],
        ['H', 'I', 'J'],
        ['K', 'A', 'B'],
        ['A', 'B', 'C']]

land = [0]*26

# DAT
for i in range(5):
    for j in range(3):
        land[ord(arr[i][j]) - 65] += 1

# 앞 인덱스 수 더하기
for i in range(len(land) - 1):
    land[i + 1] += land[i]

temp = [0]*15
print(land)
# 인덱스로 순서 정하기
for k in range(26):
    for i in range(5):
        for j in range(3):
            if chr(k +65) == arr[i][j]:
                temp[land[k] - 1] = arr[i][j]
                land[k] -= 1

for i in range(len(temp)):
    print(temp[i], end = '')