def main():
    KFC()

def KFC():
    a = chicken()
    b = coke()
    arr = []
    arr.append(a)
    arr.append(b)
    for i in arr:
        print(i,end='')

def chicken():
    a = int(input())
    return a + 10

def coke():
    a = input()
    return a

main()