def main() : 
    a = int(input())
    abc(a)

def abc(n) :
    global cnt 
    if cnt <= 3 : 
        cnt += 1
        abc(n+2)
        print(n, end = ' ')
    
cnt = 0    
main()