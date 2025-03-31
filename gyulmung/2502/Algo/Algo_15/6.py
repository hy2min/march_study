string = input()

count = 0
for i in range(len(string)):
    if i % 2 == 1: # 홀수 지정
        if string[i].islower():
            count += 1
    elif i % 2 == 0:
        if string[i].isupper():
            count += 1

if count == len(string):
    print('개구리문장')
else:
    print('일반문장')