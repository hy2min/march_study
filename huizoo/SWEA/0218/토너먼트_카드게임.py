def abc(i, j):
    if j-i == 0:
        return i
    elif j-i == 1:
        return rsp(i, j)
    else:
        return rsp(abc(i, (i+j)//2), abc((i+j)//2+1, j))

def rsp(a, b):
    aa, bb = lst[a], lst[b]
    if aa == bb:
        return a
    elif aa-bb == 1 or aa-bb == -2:
        return a
    else:
        return b

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.insert(0, 0)
    ret = abc(1, N)
    print(f'#{tc} {ret}')