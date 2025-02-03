a = int(input())

arr = [a - i for i in range(5)]

def KFC():
    global arr
    for i in arr:
        print(i,end='')

KFC()