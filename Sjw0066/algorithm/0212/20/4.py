def abc(level):

    if level == input1+6:
        print(level, end=" ")
        return


    abc(level + 2)
    print(level, end=" ")


input1 = int(input())
abc(input1)
