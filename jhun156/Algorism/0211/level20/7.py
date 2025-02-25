arr = [3,7,4,1,9,4,6,2]

index = int(input())

def abc(num):

    print(arr[num],end=' ')
    if num == 0:
        return
    abc(num-1)
    print(arr[num],end = ' ')

abc(index)