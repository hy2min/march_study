st = list(input())
dat = [0]*26
for char in st : 
    dat[ord(char)-65] += 1
for i in range(26) : 
    if dat[i] :
        print(f'{chr(i+65)}:{dat[i]}')