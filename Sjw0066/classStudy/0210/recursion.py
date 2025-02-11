#재귀함수
# N = int(input())
# def abc(level):
#
#     if level==N:
#         print(level,end=" ")
#         return
#     print(level, end=" ")
#     abc(level+1)
#     print(level, end=" ")
#
# abc(1)
#

# def abc(level):
#
#     if level==2:
#         return
#     for i in range(2):
#         abc(level+1)
#
#
#
# abc(0)

'''
위의 경우 트리의 구조를 가지는 재귀 함수로
트리의 가지수는 호출하는 함수의 개수
트리의 깊이는 종료조건으로 설정한 값에 따라 달라진다.
'''


def abc(level):

    if level==2:
        return

    for i in range(2):
        print('.')
        abc(level+1)
        print('.')
abc(0)

#소스코드위치에 따라 실행 타이밍이 너무 달라져서 잘 이해해야됨 ㅇㅇ

