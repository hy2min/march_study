n = int(input())
def devide_num(a) : 
    if a > 0 : 
        devide_num(a//2)
        print(a, end = ' ')
devide_num(n)