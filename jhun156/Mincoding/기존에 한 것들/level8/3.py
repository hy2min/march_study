def Input():
    
    a,b = map(int,input().split())

    return a + b

def output():
    
    global sum
    a = 5

    while a <= sum:
        print(a,end=' ')
        a += 1
        
sum = Input()

output()