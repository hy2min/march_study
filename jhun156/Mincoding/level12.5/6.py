def main():

    a = input()
    leng = len(a)
    count = a.count(a[leng-1])
    print(leng)
    print(count)

main()