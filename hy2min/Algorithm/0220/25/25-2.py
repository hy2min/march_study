n = int(input())
for _ in range(n):
    s = input()
    i = 0
    while i < len(s)-5:
        if s[i] == '[' and s[i+1:i+6].isdigit() and s[i+6] == ']':
            print(s[i:i+7])
            i += 7
        else:
            i += 1