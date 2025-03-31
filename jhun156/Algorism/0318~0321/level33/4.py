# import sys
# sys.stdin = open("input.txt","r")

N, K = map(int,input().split())
arr = [list(input().split()) for _ in range(N)]
lst = [i for i in range(K+1)]

def union(num1,num2):

    A,B = find(num1), find(num2)
    if type(A) == int and type(B) == int:
        if A < B:
            lst[B] = A
        else:
            lst[A] = B
    elif type(A) == int and type(B) == str:
        lst[A] = B
    elif type(A) == str and type(B) == int:
        lst[B] = A
    return

def find(num):

    if lst[num] == num:
        return num

    if type(lst[num]) == int:

        ret = find(lst[num])
        lst[num] = ret

        return ret

    else:
        return lst[num]


for i in range(N):
    # 2개의 인자값이 숫자인 경우
    a = arr[i][0]
    b = arr[i][1]
    if a.isdigit() and b.isdigit():
        # lst의 두 인덱스에 대해 집합으로 묶기
        union(int(a),int(b))
    elif a.isdigit() and type(b) == str:
        # lst의 인덱스에 대해 집합인지 확인하고
        # a 인덱스에 값 넣기
        for j in range(K+1):
            if j == int(a):
                continue
            if lst[j] == lst[int(a)]:
                lst[j] = b
        lst[int(a)] = b
    elif b.isdigit() and type(a) == str:
        for j in range(K+1):
            if j == int(b):
                continue
            if lst[j] == lst[int(b)]:
                lst[j] = a
        lst[int(b)] = a

for i in range(1,K+1):
    print(lst[i],end='')
