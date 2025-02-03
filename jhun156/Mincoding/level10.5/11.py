def main():
    a = int(input())
    lst = run(a)
    for i in lst:
        for j in i:
            print(j,end='')
        print()

def run(number):
    arr = []
    count = 1
    if number < 10:
        for i in range(3):
            row = []
            for j in range(3):
                row.append(count)
                count += 1
            arr.append(row)
    else:
        for i in range(3):
            row = []
            for j in range(3):
                row.append(count)
                count += 1
            row.reverse()
            arr.append(row)
    return arr

main()