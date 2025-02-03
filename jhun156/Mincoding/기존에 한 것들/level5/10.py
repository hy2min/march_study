def main():
    arr = [i for i in map(int,input().split())]
    arr.reverse()

    for i in arr:
        print(i,end='')

main()
