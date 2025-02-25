n = int(input())
def countdown(a) : 
    print(a, end = ' ')
    if a > 0 :  
        countdown(a-1)
        print(a, end = ' ')

countdown(n)
