group = ['A', 'E', 'E', 'A', 'E', 'B', 'C', 'C', 'D', 'A']
id = [21, 15, 6, 15, 34, 32, 35, 36, 14, 3]

data = {}
for i in range(len(group)):
    if group[i] in data:
        data[group[i]].append(id[i])
    else:
        data[group[i]] = [id[i]]

s = input()
print(*data[s])