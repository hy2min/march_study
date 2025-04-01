n = int(input())

def count_down(level):
    print(level, end = " ")

    if level == 0:
        return
    count_down(level - 1)
    print(level, end = " ")


count_down(n)