chocolate = "ABC"
cnt = 0

n = int(input())

def abc(level,string):
    global cnt
    if level == n:
        if "AAA" in string or "BBB" in string or "CCC" in string:
            return
        cnt += 1
        return
    
    for i in range(3):
        abc(level + 1, string + chocolate[i])

abc(0, "")
print(cnt)