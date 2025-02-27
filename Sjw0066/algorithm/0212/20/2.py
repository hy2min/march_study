def recursion(input1):
    if input1 == 0:
        print(input1,end=" ")
        return
    print(input1,end=" ")
    recursion(input1 - 1)
    print(input1,end=" ")

input1 = int(input())
recursion(input1)
