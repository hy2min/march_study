#재귀함수
N = int(input())
def abc(level):

    if level==N:
        return
    print(level, end=" ")
    abc(level+1)
    print(level, end=" ")

abc(0)