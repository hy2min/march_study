arr = [
    ['A', 'D', 'F'],
    ['Q', 'W', 'E'],
    ['Z', 'X', 'C']
]


def main() :
    a = input()

    a1, b1 = find(a)

    print(a1, b1, sep=",")


def find(a) :
    for i in range(3) :
        for j in range(3) :
            if arr[i][j] == a :
                return i, j
            

main()