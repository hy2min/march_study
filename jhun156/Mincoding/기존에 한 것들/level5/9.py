arr = ['A','B','C']
a = 0

def KFC():
    for i in arr:
        print(i,end='')
    print()

def main():
    global a
    a = int(input())
    while a > 0:
        KFC()
        a -= 1

main()