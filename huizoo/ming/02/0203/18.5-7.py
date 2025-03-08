vect = 'MINCODING'
n = int(input())
arr = input().split()
# for alp in arr : 
#     if alp in vect : 
#         print('o', end="")
#     else : 
#         print('x', end="")
dat=[0]*26
for char in vect : 
    dat[ord(char)-65] = 1

for alp in arr : 
    if dat[ord(alp) - 65] : 
        print('O', end="")
    else :
        print('X', end="")
