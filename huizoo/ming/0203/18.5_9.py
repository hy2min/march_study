st = list(input())
dat = [0]*26
for char in st : 
    dat[ord(char)-65] += 1
# for i in range(26) :
#     while dat[i] >= 2 : 
#         st.remove(chr(i+65))
#         dat[i] -= 1
# print(''.join(sorted(st)))
st = [char for char in st if dat[ord(char) -65] < 2]
print(''.join(sorted(st)))