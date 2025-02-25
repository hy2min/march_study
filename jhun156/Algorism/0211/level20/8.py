a = int(input())

def cross(num):

    if num == 0:
        return
    cross(num//2)
    print(num,end=' ')

cross(a)