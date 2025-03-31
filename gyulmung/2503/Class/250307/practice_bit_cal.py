# a = 13
# b = bin(a)
# c = oct(a)
# d = hex(a)
# print(a, b, c, d)
# print(type(b)) # str 타입
# print(b[2:])
# print(int(b, 2))
# print(int(c, 8))
# print(int(d, 16))
#
# def trans(value):
#     ans = ''
#     while value >= 1:
#         value,rest = divmod(value, 3)
#         ans+=str(rest)
#     ans = ans[::-1]
#     return ans
#
# ret = trans(a)
# print(ret)
# print(int(ret, 3))


# 속도를 중요하게 생각하는 작업 시 비트연산자를 바로 작성해주면 된다.
print(13&9) # ampersand : 둘다 1이면 참 - 9
print(13|9) # bar : 둘 중 하나만 1이면 참 - 13
print(13^9) # caret : 'exclusive or' 연산 - 4

# shift연산
# 10 << 2 1010 --> 101000 : 10 * 2**2
# 10 >> 2 1010 --> 0010 : 10 // 2**2
print(10 << 2)
print(10 >> 1)
# 부분집합계산시 shift연산자를 이용한다.
arr=[1,2,3]
n=3
for i in range(1<<3):
    answer=[]
    for index in range(3):
        if i&(1<<index)!=0:
            answer.append(arr[index])
    if answer:
        print(answer)
