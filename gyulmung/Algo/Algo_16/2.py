arr = [['A', 'B', 'K', 'T'], ['K', 'F', 'C', 'F'], ['B', 'B', 'Q', 'Q'], ['T', 'P', 'Z', 'F']]

st1, st2 = map(str, input().split())
count1, count2 = 0, 0

for i in arr:
    for j in i:
        if st1 == j:
            count1 += 1
        if st2 == j:
            count2 += 1
print(count1 + count2)