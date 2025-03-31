town = [['C', 'D', 'A'], ['B', 'M', 'Z'], ['Q', 'P', 'O']]
Black_list = list(map(str, input()))

lst = [0]*26
count = 0

for i in range(3):
    for j in range(3):
        lst[ord(town[i][j])-65] += 1

for i in range(4):
    for j in range(26):
        if lst[j] != 0 and j == ord(Black_list[i]) - 65:
            count += 1

print(f'{count}명')