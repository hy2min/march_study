import sys
sys.stdin = open('input.txt','r')

num = int(input())
n = int(input())
cnt = 0
ret = 0
while 1:
    if cnt == n:
        break
    num = int(num)*2
    num = str(num)
    num = num[::-1]
    cnt += 1
print(num)