import sys
sys.stdin = open("input.txt", "r")

T=int(input())

def hex_to_bin(str1):
    for i in range(len(str1)):
        for j in range(16):
            if hex_num[j] == str1[i]:
                n = j
                binary_temp = ''
                while n:
                    binary_temp = str(n % 2) + binary_temp
                    n = n // 2
    return  binary_temp.zfill(4)

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
    arr=[input() for _ in range(N)]
    arr=list(set(arr))
    hex_num='0123456789ABCDEF'
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

    for i in range(1,len(arr)):
        changed_input=''
        for j in range(M):
            ret=hex_to_bin(arr[i][j])
            changed_input+=ret
        changed_input=changed_input.rstrip('0')

        index=len(changed_input)
        c1,c2,c3,c4=0,0,0,0
        for k in range(index-1,-1,-1):
            if c3==0 and changed_input[k]=='1':
                c4+=1
            elif c2==0 and changed_input[k]=='0':
                c3+=1
            elif c1==0 and changed_input[k]=='1':
                c2+=1
            elif changed_input[k] == '0':
                if changed_input[k-1] == '1':
                    power = min(c2 , c3 , c4)
                    changed_int.append(code[c2//power,c3//power,c4//power])
                    if len(changed_int)==8:
                        answer=check_code(changed_int)
                        if answer:
                            if changed_int not in visited:
                                visited.append(changed_int)
                                final_answer+=sum(changed_int)

                        changed_int=[]
                    c2,c3,c4=0,0,0


    print(f'#{tc} {final_answer}')













