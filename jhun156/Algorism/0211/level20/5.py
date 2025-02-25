arr = list(input())

def abc(num):

    print(arr[num],end='')
    if num == 4:
        print()
        print(arr[num],end='')
        return
    abc(num+1)
    print(arr[num],end='')

abc(0)