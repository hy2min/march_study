def main():
    
    a = getChar()
    print(a)

def getChar():

    t1,t2 = input().split()

    a = max(ord(t1),ord(t2))

    return chr(a)

main()