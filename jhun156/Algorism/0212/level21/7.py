str1 = input()
N = len(str1)

def abc(num):

    global N
    print(num, end=' ')
    if num == 1:
        return
    abc(num-1)
    print(num,end=' ')

abc(N)