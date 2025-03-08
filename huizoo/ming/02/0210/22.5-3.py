a = input()
arr = [[[0]*3 for _ in range(3)] for _ in range(3)]
a_ascii = ord(a)
for i in range(3) :
    arr[i] = [[chr(a_ascii+i)]*3 for _ in range(3)]
    print('\n'.join(''.join(row) for row in arr[i]))
    print()
