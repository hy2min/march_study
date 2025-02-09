vect = ['M','I','N','C','O','D','I','N','G']
lst = [0]*26

find_number = int(input())
find_str = list(map(str, input().split()))

for i in range(len(vect)):
    lst[ord(vect[i]) - 65] += 1

for i in range(find_number):
    if lst[ord(find_str[i]) - 65] != 0:
        print('O', end = "")
    else:
        print('X', end = '')