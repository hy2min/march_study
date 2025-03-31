oil = input()


def binary_search(st, ed):
    Max = -1
    while 1:
        mid = (st + ed) // 2

        if oil[mid] == '#':
            st = mid + 1
            Max = mid
        if oil[mid] != '#':
            ed = mid - 1

        if st > ed:
            break
    return Max+1


answer = binary_search(0, len(oil)-1)

print(f'{answer * 10}%')
