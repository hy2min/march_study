s = input()
alp = "ABCD"
cnt = 0

def abc(level, string):
    global cnt
    if level == 3:
        cnt += 1
        if string == s:
            print(f'{cnt}번째')
        return 
    
    for i in range(4):
        abc(level + 1, string + alp[i])

abc(0,"")