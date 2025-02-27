def main():
    str1=input()
    len1=stringLen(str1)
    
    print(f'{len1}글자')

def stringLen(str1):
    result=0
    for i in str1:
        result+=1
    return result

main()