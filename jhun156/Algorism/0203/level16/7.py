a = input()
b = input()
c = input()
lst = [a,b,c]
result = 0

for i in range(3):
    temp = lst[i].count('M')
    result += temp

if result == 0:
    print("M이 존재하지 않습니다")
else:
    print("M이 존재합니다")