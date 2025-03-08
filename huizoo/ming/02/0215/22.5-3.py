alp = input()
arr = [[[chr(ord(alp)+i)]*3 for _ in range(3)] for i in range(3)]

for i in range(3):
    print('\n'.join(''.join(row) for row in arr[i]))
    print()
