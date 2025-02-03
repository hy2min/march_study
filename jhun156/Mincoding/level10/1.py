def one():

    a = int(input())
    return a

def two():

    a = input()
    return a

def main():

    arr =[]
    a = one()
    b = two()
    arr.append(a)
    arr.append(b)
    for i in arr:
        print(i,end='')

main()
