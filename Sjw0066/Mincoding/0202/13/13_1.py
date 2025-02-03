def getName(str1):

    if ord(str1[0]) < ord(str1[1]):
        return 0
    else :
        return 1
    
def main():
    str1=list(map(str,input().split()))
    result=getName(str1)
    print(str1[result])

main()    
