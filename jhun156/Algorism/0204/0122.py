# 매개변수(parameter) : 함수를 정의할 때, 함수가 받을 값을 나타내는 변수
# 인자(argument) : 함수를 호출할 때, 실제로 전달되는 값
# 다양한 인자 종류
# 1. 위치 인자, 2. 기본 인자 값, 3. 키워드 인자, 4. 임의의 인자 목록, 5. 임의의 키워드 인자 목록

# 1. 위치인자(Positional Arguments)
# 함수 호출 시 인자의 위치에 따라 전달되는 인자
# 위치인자는 함수 호출 시 반드시 값을 전달해야함

# 2. 기본인자값(Default Argument Values)
# 함수 정의에서 매개변수에 기본 값을 할당하는 것
# 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨

# 3. 키워드 인자(Keyword Arguments)
# 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
# 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
# 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
# 단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함

# 4. 임의의 인자 목록(Arbitrary Argument Lists)
# 정해지지 않은 개수의 인자를 처리하는 인자
# 함수 정의 시 매개변수 앞에 '*'를 붙여 사용
# 여러 개의 인자를 tuple로 처리

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# map(function, iterable)
# numbers = [1,2,3]
# result = map(str,numbers)
# print(result)
# print(list(result))

# zip(*iterables)
# girls = ['jane','ashley']
# boys = ['peter','jay']
# pair = zip(girls,boys)
# print(dict(pair))

# kr_scores = [1,2,3,4]
# math_scores = [2,4,5,7]
# en_scores = [4,3,3,5]
# for student_scores in zip(kr_scores,math_scores,en_scores):
#     print(student_scores)
# scores = [
#     [1,2,3],
#     [4,5,3],
#     [2,4,5],
# ]

# for score in zip(*scores):
#     print(score)
# 10,2,3
# 10,2,500
# 1,2

# lambda 매개변수 : 표현식

def addition(x,y):
    return x + y

result = addition(3,5)
print(result)

addition = lambda x, y : x + y
result = addition(3,5)
print(result)

numbers = [1,2,3,4,5]

squared = list(map(lambda x : x **2, numbers))
print(*squared)