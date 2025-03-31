def abc(num):

    global X,Y

    if num == 2:
        print(X,end='')
        print(Y,end='')
        print()
        return

    for i in range(65,68):
        if num == 0:
            X = chr(i)
        if num == 1:
            Y = chr(i)
        abc(num+1)

X,Y = 0,0
abc(0)