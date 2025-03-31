# 재귀 호출(재귀함수)(recursion)
# : 어떠한 함수가 자기자신을 계속 호출하는 형태

# 0 1 2 출력하기

Max = int(input())

def abc(level):
    if level == Max:
        return

    print(level, end = ' ')
    abc(level + 1)
    print(level, end = ' ')

abc(0)