st = input()
a, b = input().split()
dx = [-1, 1]
st2 = st
for i in range(len(st)) : 
    if st[i] == a or st[i] == b : 
        for j in range(2) : 
            ni = i + dx[j]
            if 0 <= ni < len(st) :
                st2 = st2.replace(st[ni], '#')

print(st2)
