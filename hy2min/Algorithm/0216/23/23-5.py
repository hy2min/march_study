s = input()

member = "EWABC"
cnt = 0
path = [""] * 4
used = [0] * len(member)

def abc(level=0, string=""):
    global cnt
    if level == 4:
        if s not in string:
            print(string)
            return
    
    for i in range(5):
        if not used[i]:
            used[i] = 1
            abc(level+1, string+member[i])
            used[i] = 0

abc()