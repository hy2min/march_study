def recursion(level):

    if level>len(input1):
        return
    print(input1[:level])
    recursion(level+1)


input1=input()
recursion(1)