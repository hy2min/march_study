a=input()
DAT=[0]*26
for i in range(len(a)):
    DAT[ord(a[i])-ord('A')]+=1
for i in range(26):
    if DAT[i]!=0:
        print(chr(i+ord('A')),end='')