a,b = input().split()

# a = 행번호, b = 채울문자

arr = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

count = ord(b)

for i in range(4,-1,-1):
    arr[int(a)-1][i] = chr(count)
    count += 1

for i in arr:
    for j in i:
        print(j,end='')
    print()