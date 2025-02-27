def main():
    str1 = input()
    str2 = input()
    result=FindABC(str1,str2)

    print(f'A:{result["A"]}')
    print(f'B:{result["B"]}')
    print(f'C:{result["C"]}')

def FindABC(str1,str2):
    cnt_a=0
    cnt_b=0
    cnt_c=0

    for i in str1 :
        if i == 'A':
            cnt_a += 1
        elif i == 'B':
            cnt_b += 1
        elif i == 'C':
            cnt_c += 1    

    for i in str2 :
        if i == 'A':
            cnt_a += 1
        elif i == 'B':
            cnt_b += 1
        elif i == 'C':
            cnt_c += 1
    return {'A':cnt_a,'B':cnt_b,'C':cnt_c}

main()