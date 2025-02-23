arr = ['M','I','N','Q','U','E','S','T']

def Length(char):
    for i in range(len(arr)):
        if arr[i] == char:
            return i  

def main() : 
    a = input()
    b = input()
    c = input()

    indices1 = Length(a)
    print(f"{a}={indices1}")

    indices2 = Length(b)
    print(f"{b}={indices2}")

    indices3 = Length(c)
    print(f"{c}={indices3}")

main()
    