def overlap(s):
    check = []
    for char in s:
        if char in check:
            return 0
        check.append(char)
    return 1

n = int(input())
for _ in range(n):
    s = input()
    
    ans = True
    start = True
    temp = ''
    
    for char in s:
        if char == '<':
            start = True
            temp = ''
        elif char == '>':
            if not overlap(temp):
                ans = False
            start = False
        elif start:
            temp += char
    if ans:
        print('O', end="")
    else:
        print('X', end="")