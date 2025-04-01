# GCD: 최대공약수
# 최대 공약스 - 2부터 두 숫자 중 작은 수까지 나누었을 때
# 나눠지는 가장 큰 값
# --> 유클리드 호제법 : 세계 최초의 알고리즘

gcd = 0
answer = 0
a, b = map(int, input().split())

while b:
    answer = a % b
    a = b
    b = answer
print(a)
gcd = a


# LCM: 최소공배수
a, b = map(int, input().split())
LCM = gcd*((a//gcd)*(b//gcd))
print(LCM)