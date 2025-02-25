
def main() : 
    a = input()
    b = input()

    a1,b1,c1 = FindABC(a,b)

    print(f"A:{a1}")
    print(f"B:{b1}")
    print(f"C:{c1}")



def FindABC(a,b) :
    arr_a = [*a]
    arr_b = [*b]

    a1 = arr_a.count("A") + arr_b.count("A")
    b1 = arr_a.count("B") + arr_b.count("B")
    c1 = arr_a.count("C") + arr_b.count("C")

    return a1,b1,c1


main()