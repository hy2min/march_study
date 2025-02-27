def recursion(index):
    if index == len(input1)-1:
        print(input1[index], end=" ")
        return
    print(input1[index], end=" ")
    recursion(index + 1)
    print(input1[index], end=" ")


input1 = list(map(int, input().split()))
recursion(0)
