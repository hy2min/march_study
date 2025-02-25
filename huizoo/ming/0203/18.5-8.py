st_list = [input() for _ in range(3)]
dat = [0]*26
flag = 0
for st in st_list :
    for char in st : 
        if dat[ord(char)-65] :
            flag = 1
        else : 
            dat[ord(char)-65] = 1
if flag : 
    print('No')
else : 
    print('Perfect')