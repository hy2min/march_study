lst = input().split()
arr = []
for i in range(3):
    arr.append(ord(lst[i]) + 1)

for i in arr:
    print(chr(i),end= ' ')

# 포인터 문제라 답만 구했습니다.