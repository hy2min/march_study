n = int(input())

def count_down(num):

    print(num, end=' ')
    num -= 1
    if num == -1:
        return
    count_down(num)
    print(num+1, end=' ')

count_down(n)