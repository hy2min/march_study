a= input()

if ord(a) >= ord('a') and ord(a) <= ord('z'):
    print("소문자입력!!")
elif ord(a) >= ord('A') and ord(a) <= ord('Z'):
    print("대문자입력!!")
elif ord(a) >= ord('0') and ord(a) <= ord('9'):
    print("숫자문자입력!!")

