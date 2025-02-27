str1=input()
for i in range(len(str1)-1,-1,-1):
    for j in range(len(str1)):
        if j <= i:
            print(str1[i:], end='')
            break
    print()
