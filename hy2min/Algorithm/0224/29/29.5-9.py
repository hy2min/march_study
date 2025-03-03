s1=input()
s2=input()

max_len = 0
max_str = ''

for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        sub = s1[i:j]
        if sub in s2 and len(sub) > max_len:
            max_len = len(sub)
            max_str = sub

print(max_str)