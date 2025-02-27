IDPW = ['qlqlaqkq', 'tkaruqtkf']
Input_ID = input()
Input_PW = input()
Input = [Input_ID, Input_PW]
def ID_PW(level):
    if level == 2:
        print('LOGIN')
        return

    elif IDPW[level] != Input[level]:
        return print('INVALID')

    ID_PW(level + 1)

ID_PW(0)
