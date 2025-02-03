def main():
    rnt = yesOrNo()
    print(rnt)

def yesOrNo():
    a = int(input())
    if a % 3 == 0:
        return 7
    elif a % 3 == 1:
        return 35
    else:
        return 50

main()