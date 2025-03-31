import sys
sys.stdin = open("input.txt", "r")

T=int(input())

def check_code(lst):
    ret2=0
    rev_lst=list(reversed(lst))
    for i in range(len(rev_lst)):
        if i%2==0:
            ret2+=rev_lst[i]*3
        else:
            ret2+=rev_lst[i]

    if ret2%10==0:
        return ret2
    else:
        return False

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr1=[input() for _ in range(N)]
    arr=list(set(arr1))
    for i in range(len(arr)):
        arr[i]=arr[i].rstrip('0')

    code={
        (2,1,1):0,
        (2,2,1):1,
        (1,2,2):2,
        (4,1,1):3,
        (1,3,2):4,
        (2,3,1):5,
        (1,1,4):6,
        (3,1,2):7,
        (2,1,3):8,
        (1,1,2):9,
    }

    changed_int=[]
    visited=[]
    final_answer=0

    c1,c2,c3,c4=0,0,0,0
    for i in range(len(arr)):
        if arr[i]:
            for j in range(len(arr[i])-1,-1,-1):
                if c3==0 and arr[i][j]=='1':
                    c4+=1
                elif c2==0 and arr[i][j]=='0':
                    c3+=1
                elif c1==0 and arr[i][j]=='1':
                    c2+=1
                elif arr[i][j] == '0':
                    if arr[i][j-1] == '1':
                        changed_int.append(code[c2,c3,c4])
                        if len(changed_int)==8:
                            answer=check_code(changed_int)
                            if answer:
                                if changed_int not in visited:
                                    visited.append(changed_int)
                                    final_answer+=sum(changed_int)
                            changed_int=[]
                        c2,c3,c4=0,0,0

    print(f'#{tc} {final_answer}')













