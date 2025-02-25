s = "ABC"

def abc(level,string):
    if level == 2:
        print(string)
        return
    for i in range(3):
        abc(level + 1, string + s[i])
abc(0,"")