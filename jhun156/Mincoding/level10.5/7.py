def main():
    rnt = aToZ()
    print(rnt)

def aToZ():
    
    a = input()

    if (ord(a)-ord('A')) > (ord('Z')-ord(a)):
        return 'Z'
    else:
        return 'A'

main()