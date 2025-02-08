lst = [
    ['A','B','G','K'],
    ['T','T','A','B'],
    ['A','C','C','D'],
]

pattern = [[i for i in list(input())] for _ in range(2)]

def find_pattern(y,x):
    for i in range(2):
        for j in range(2):
            if lst[y+i][x+j] != pattern[i][j]:
                return 0
    return 1

result = 0
for i in range(2):
    for j in range(3):
        ans = find_pattern(i,j)
        result += ans

if result > 0:
    print(f"발견({result}개)")
else:
    print("미발견")