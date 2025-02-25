arr = [
    ['A', 'B', 'K', 'T'],
    ['K', 'F', 'C', 'F'],
    ['B', 'B', 'Q', 'Q'],
    ['T', 'P', 'Z', 'F'],
]

str1, str2 = input().split()
cnt = 0
for i in arr:
    cnt += i.count(str1)
    cnt += i.count(str2)

print(cnt)
