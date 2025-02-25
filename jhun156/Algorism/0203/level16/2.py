arr = [
    ['A','B','K','T'],
    ['K','F','C','F'],
    ['B','B','Q','Q'],
    ['T','P','Z','F'],
]

lst = list(input().split())
result = 0
for chr in lst:
    for i in range(4):
        temp = arr[i].count(chr)
        result += temp
print(result)