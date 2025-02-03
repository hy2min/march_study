arr = [
    ['4','5','7','1','3','2'],
    ['D','F','Q','W','G','Z'],
]

num = int(input())

for i in range(6):
    if int(arr[0][i]) == num:
        print(arr[1][i])
    