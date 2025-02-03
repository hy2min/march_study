def main():
    rnt = Calculator()
    print(rnt)

def Calculator():

    a = int(input())
    if a >= 90:
        return "A"
    elif a >= 80:
        return "B"
    elif a >= 70:
        return "C"
    else:
        return "D"
    
main()