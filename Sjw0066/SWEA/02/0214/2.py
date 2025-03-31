def erase_double(str1):
    i=0
    while 1:

        if str1[i] == str1[i+1]:
            str1.pop(i)
            str1.pop(i)
            i=0
        else:
            i+=1

        if i == len(str1)-1 or str1==[] :
            break

    return len(str1)

T = int(input())

for tc in range(1, T + 1):
    s = list(input())

    print(f'#{tc} {erase_double(s)}')