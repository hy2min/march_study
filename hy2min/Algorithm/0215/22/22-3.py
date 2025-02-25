n = int(input())
str = "BGTK"

def abc(level,string):
    if level == n:
        print(string)
        return
    for i in range(4):
        abc(level+1, string+str[i])

abc(0,"")