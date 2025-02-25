# 모듈 : 한 파일로 묶인 변수와 함수의 모음, 특정한 기능을 하는 코드가 작성된 파이썬 파일
# import math
# print(math.sqrt(4))
# from math import sqrt
# print(sqrt(4))
# 패키지 : 연관된 모듈들을 하나의 디렉토리에 모아 놓은 것

# import requests

# url = ""
# response = requests.get(url).json()
# print(response)

# enumerate(iterable, start = 0)

fruits = ['apple','banana','cherry']

for index, fruit in enumerate(fruits):
    print(fruit,index)