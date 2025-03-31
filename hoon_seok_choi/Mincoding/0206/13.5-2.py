header = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
body = [4, 2, 5, 1, 6, 7, 3]


a,b = map(str, input().split())

a_index = header.index(a)
b_index = header.index(b)

far = abs(a_index - b_index)

how_far = 0

if a_index < b_index :
    for i in range(a_index + 1, b_index) :
        how_far += body[i]

else :
    for i in range(b_index + 1, a_index) :
        how_far += body[i]

print(how_far)
