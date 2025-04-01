import sys
sys.stdin = open('input.txt', 'r')

# 17분

Test = int(input())

for i in range(1, Test + 1):

    string = input()
    mid_num = len(string) // 2
    Flag = True

    if len(string) % 2 == 0:
        for j in range(mid_num):
            if string[mid_num + j] != string[mid_num-j-1]:
                Flag = False
    else:
        for j in range(1, mid_num+1):
            if string[mid_num + j] != string[mid_num -j]:
                Flag = False
    if Flag:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')