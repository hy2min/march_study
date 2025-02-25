def sharp(s):
    for i in range(len(lst)):
        if lst[i] == s:
            if i > 0:
                lst[i-1] = "#"
            if i < len(lst)-1:
                lst[i+1] = "#"

lst = list(input())
s1, s2 = input().split()

sharp(s1)
sharp(s2)

print("".join(lst))