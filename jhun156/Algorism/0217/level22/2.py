str1 = input()
str2 = input()
str3 = input()

def check(a,b,c):
    cnt = 0
    i = 0
    while True:
        if a == b:
            cnt += 1
            i += 1
        elif a == c:
            cnt += 1
            i += 1
        else:
            i += 1
        if i == 2:
            break
    if cnt == 2:
        return "WOW"
    elif cnt == 1:
        return "GOOD"
    else:
        return "BAD"

ans = check(str1,str2,str3)
print(ans)