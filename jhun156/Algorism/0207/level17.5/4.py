arr = [
    ['G','K','T'],
    ['P','A','C'],
]

lst = list(input().split())

def isExist(str):
    for i in range(2):
        for j in range(3):
            if arr[i][j] == str:
                return 1
    return 0

ans = 0
for i in range(2):
    k = isExist(lst[i])
    ans += k

if ans == 2:
    print("대발견")
elif ans == 1:
    print("중발견")
else:
    print("미발견")