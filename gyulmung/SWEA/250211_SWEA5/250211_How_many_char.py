import sys
sys.stdin = open('input.txt', 'r')

test = int(input())

def Find_same(string1, string2):
    Max = -1e8
    for i in range(0, len(string1)):
        count = 0
        for j in range(i + 1, len(string2)):
            if string1[i] == string2[j]:
                count += 1
            if Max < count:
                Max = count
    return Max

for j in range(1, test+1):
    str1 = input()
    str2 = input()
    str_max = Find_same(str1, str2)
    print(f'#{j} {str_max}')
