def abc(level):

    if level==1:
        print(level,end=" ")
        return
    print(level,end=" ")
    abc(level-1)
    print(level,end=" ")

str1=input()
len_str1=len(str1)

abc(len_str1)

