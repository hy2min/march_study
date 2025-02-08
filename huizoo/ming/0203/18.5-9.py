st = list(input())
dat = [0]*26
for char in st : 
    dat[ord(char)-65] += 1
for i in range(26) :
    while dat[i] >= 2 : 
        st.remove(chr(i+65))
        dat[i] -= 1

# result =[]
# for char in st : 
#     if dat[ord(char) -65] > 0 :
#         result.append(char)
#         dat[ord(char)-65] = 0

print(''.join(sorted(st)))

