PW = ['Jason', 'Dr.tom', 'EXEXI', 'GK12P', 'POW']
in_pw = input()

def find_pw(lev):
    if lev == 5:
        print('암호틀림')
        return

    if PW[lev] == in_pw:
        print('암호해제')
        return

    find_pw(lev + 1)

find_pw(0)