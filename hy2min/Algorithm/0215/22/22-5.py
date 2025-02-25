n = int(input())

def abc(level,seq):
    if level == 4:
        print(seq)
        return
    
    for i in range(1, n+1):
        abc(level+1, seq + str(i))

abc(0,"")