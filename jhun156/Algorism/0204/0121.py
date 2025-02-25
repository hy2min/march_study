# 단일 요소 튜플을 만들때는 반드시 후행 쉼표 (trailing comma 사용)
# my_tuple_1 = (1,)
my_set_1 = {1,2,3}
my_set_2 = {3,6,9}
my_set_1 | my_set_2 # 합집합
my_set_1 - my_set_2 # 차집합
my_set_1 & my_set_2 # 교집합
# 암시적 형변환 
# 1. 정수와 실수의 연산에서 정수가 실수로 변환됨
# 2. Boolean과 Numeric Type에서만 가능
print('Gildong' + 'Hong')
print('hi'*5)
print([1,2]+['a','b'])
print([1,2]*2)
x = (1,)