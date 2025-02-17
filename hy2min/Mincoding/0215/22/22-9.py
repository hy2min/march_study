passwords = ['Jason','Dr.tom','EXEXI','GK12P','POW']
s = input()
def abc(level, i):
    if level == len(passwords):
        print("암호틀림")
        return
    
    if s == passwords[i]:
        print("암호해제")
        return
    
    abc(level+1, i+1)

abc(0,0)