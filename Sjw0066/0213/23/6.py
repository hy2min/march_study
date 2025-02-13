lst1=[3,5,1,9,7]


def abc(level):
    if level==4:
        print(*lst1)
        return
    direct = input()
    if direct=='R':
        temp=lst1[4]
        for i in range(len(lst1)-1,0,-1):
            lst1[i]=lst1[i-1]
        lst1[0]=temp
    if direct=='L':
        temp=lst1[0]
        for i in range(len(lst1)-1):
            lst1[i]=lst1[i+1]
        lst1[4]=temp
    abc(level+1)

abc(0)