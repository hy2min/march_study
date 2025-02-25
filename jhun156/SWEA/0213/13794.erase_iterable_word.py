# import sys
# sys.stdin = open("input.txt","r")

def iterable_word(string):
    lst = list(string)
    n = len(lst)
    tmp = -1
    if n == 1:
        return string
    else:
        for i in range(n-1):
            if lst[i] == lst[i+1]:
                tmp = i
                break
    if tmp == -1:
        return string
    else:
        for i in range(2):
            lst.pop(tmp)
        tmp = ''
        for i in range(len(lst)):
            tmp += lst[i]
        ans = iterable_word(tmp)
        return ans

T = int(input())
for tc in range(1,T+1):
    array = input()
    ans = iterable_word(array)
    print(f"#{tc} {len(ans)}")