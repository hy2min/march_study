str1=input()


for i in range(-3,4):
    answer = ord(str1) + i
    if answer > ord('Z') :
        answer -=  26
    if answer< ord('A'):
        answer += 26
    print(chr(answer))