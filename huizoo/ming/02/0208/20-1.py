def main() : 
    bbq(5)
    

def bbq(a):
    if a > 0:
        bbq(a - 1)
        
main()