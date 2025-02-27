def main():
    age=int(input())
    result=[]
    result=moom(age)
    print(*result)

def moom(age):
    result=[]

    result.append(age-4)
    result.append(age+3)
    result.append(age*2)
    return result

main()