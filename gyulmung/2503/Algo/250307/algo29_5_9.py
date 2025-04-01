A = input()
B = input()
if len(A) > len(B):
    Max = A
    Min = B
elif len(A) <= len(B):
    Max = B
    Min = A

Max_arr = ''

def Find(y):
    cnt = 0
    for i in range(len(ak)):
        if i + y >= len(Max): continue
        if ak[i] == Max[i + y]:
            cnt += 1
    if cnt == len(ak):
        return ak
    else:
        return '0'

for i in range(len(Min)-1):
    for j in range(i+1):
        ak = Min[j:len(Min)-i+j]

        for k in range(len(Max)):
            if Max[k] == ak[0]:
                ret = Find(k)
                if len(Max_arr) < len(ret):
                    Max_arr = ret

print(Max_arr)