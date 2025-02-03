def main():
    a = input()
    b = input()
    num1,num2,num3 = FindABC(a,b)
    print(f"A:{num1}\nB:{num2}\nC:{num3}")

def FindABC(str1,str2):
    A,B,C = 0,0,0
    for i in range(len(str1)):
        if str1[i] == 'A':
            A += 1
        elif str1[i] == 'B':
            B += 1
        elif str1[i] == 'C':
            C += 1
    for i in range(len(str2)):
        if str2[i] == 'A':
            A += 1
        elif str2[i] == 'B':
            B += 1
        elif str2[i] == 'C':
            C += 1
    return A,B,C

main()