lst = [list(map(str, input())) for _ in range(4)]
arr = [['A', 'B', 'C', 'D'],
       ['B', 'B', 'A', 'B'],
       ['C', 'B', 'A', 'C'],
       ['B', 'A', 'A', 'A']]
gold = [0]*4

print(lst)
for i in range(4):
    for j in range(4):
        if lst[i][j] == arr[i][j]:
            gold[ord(lst[i][j]) - 65] += 1
result = gold.index(max(gold))
print(chr(result+65))

