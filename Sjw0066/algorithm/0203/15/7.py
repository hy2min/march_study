arr=['A','B','C','Z','E','T','Q']

bad_man=list(input())

for i in bad_man:
    if i in arr:
        print(f'{i}=마을사람')
    else:
        print(f'{i}=외부사람')
    
