arr1 = ['B','D','5','Q','A']
arr2 = ['Q','E','R','E','F']

def Input():

    a = input()

    return a

def output(a):

    global arr1,arr2

    if a.islower():
        for i in arr1:
            print(i,end='')
    elif a.isupper():
        for i in arr2:
            print(i,end='')
    else:
        print("HGFEDCBA")

STR = Input()
output(STR)