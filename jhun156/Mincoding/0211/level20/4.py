a = int(input())

def abc(num):

    global a

    if num == a + 2 * 4:
        return
    abc(num+2)
    print(num, end = ' ')

abc(a)