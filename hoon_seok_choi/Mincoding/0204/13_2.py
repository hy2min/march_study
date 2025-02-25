def main() :
    age = int(input())

    age1, age2, age3 = moom(age)

    print(age1, age2, age3)


def moom(age) :
    age1 = age -4
    age2 = age +3
    age3 = age *2

    return age1, age2, age3


main()
#test