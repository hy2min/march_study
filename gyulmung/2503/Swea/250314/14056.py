import sys
sys.stdin =open('input.txt','r')

def tree(lev):
    global ret, cnt
    if lev>N:
        return

    tree(lev*2)
    ret[lev] = cnt
    cnt+=1
    tree(lev*2+1)
T = int(input())
for test in range(1, T+1):
    N = int(input())
    idx = N //2
    ret = [0]*(N+1)
    cnt = 1
    tree(1)
    print(f'#{test} {ret[1]} {ret[idx]}')
