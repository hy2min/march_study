import sys
sys.stdin=open('input.txt','r')

lst = list(input())
num = int(input())

a_len = len(lst)

for i in range(num % a_len):
    temp = lst[-1]
    for i in range(a_len-1, 0, -1):
        lst[i] = lst[i-1]
        lst[0]=temp

print(''.join(lst))