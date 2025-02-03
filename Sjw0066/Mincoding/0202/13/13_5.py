def main():
    str1=input()
    upper_cnt,lower_cnt=KFC(str1)
    
    print(f'대문자{upper_cnt}개')
    print(f'소문자{lower_cnt}개')

def KFC(str1):
    upper_cnt=0
    lower_cnt=0
    for i in str1:
        if i.isupper():
            upper_cnt+=1
        else :
            lower_cnt+=1
    return upper_cnt,lower_cnt

main()