max_len=-21e8
min_len=21e8

max_index=0
min_index=0

for i in range(4):
    str1=input()
    len_str1=len(str1)
    if len_str1>max_len:
        max_len=len_str1
        max_index=i
    if len_str1<min_len:
        min_len=len_str1
        min_index=i

print(f'긴문장:{max_index}')
print(f'짧은문장:{min_index}')