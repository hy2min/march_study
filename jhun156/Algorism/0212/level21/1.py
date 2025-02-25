def abc(num):

    if num == 2:
        return

    for i in range(3):
        abc(num+1)

abc(0)